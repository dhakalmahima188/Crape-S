from django.shortcuts import render
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from news.models import files
from django.core.files import File
from urllib.parse import urlparse
import fitz
from PyPDF2 import PdfFileReader, PdfFileWriter



def language(filepath):
    from langdetect import detect
    from pdfminer3.layout import LAParams
    from pdfminer3.pdfpage import PDFPage
    from pdfminer3.pdfinterp import PDFResourceManager
    from pdfminer3.pdfinterp import PDFPageInterpreter
    from pdfminer3.converter import TextConverter
    import io
    i=0
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(filepath, 'rb') as fh:

        for page in PDFPage.get_pages(fh,
                                    caching=True,
                                    check_extractable=True):
            page_interpreter.process_page(page)

        texts = fake_file_handle.getvalue()
    

    # close open handles
    converter.close()
    fake_file_handle.close()

    # print(text)
    special_characters = "!@#$%^&*()-+?_=,<>/[]{}|\~`"
    # texts="My name %5 मेरो नाम महिमा ढकाल हो |"
    j=0
    n_count=0
    e_count=0
   
    text=texts.split(' ')
    # print(text)
    for txt in text:
        txt=text[j]
        if any(c in special_characters for c in txt) or  txt.isnumeric()==True :       
            # print(txt) 
            
            j=j+1     
            
            continue
        else:
            if(len(txt)>=5 and len(txt)<=10):
                # print(txt)
                if (detect(txt)=='ne' or detect(txt)=='hi'):
                    n_count=n_count+1
                else:
                    e_count=e_count+1   
        j=j+1  
    # print("Nepali:", n_count)
    # print("English:" ,e_count) 
    if(n_count>e_count):
       return "Nepali"
    else:
       return "English" 



list=[]

urls = ['http://mohp.gov.np/', 'http://nepalindata.com/resource/category/laws-policies-and-strategies/', 'http://nepalconsular.gov.np/np/',
        'http://www.dotm.gov.np/', 'http://mofa.gov.np/', 'http://merolagani.com/', 'http://www.dop.gov.np/', 'http://ciaa.gov.np/','http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html']
i=0

# urls=['http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html']

for url in urls:
    print(url)

    drive='D:\\'
    folder='data'
 
    urlparse(url)
    folders=urlparse(url).netloc
    if(folders.split('.')[0]=='www'):
        directory = folders.split('.')[1]
    else:
        directory=folders.split('.')[0]


    folder_location = os.path.join(drive,folder,directory)

    # print(folder_location)
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")     

    for link in soup.select("a[href$='.pdf']"):
    
        #sees anchor tag , check hrefs,$ means end of the string and at end searches .pdf extension
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        print(filename)
        # print(i)
        # for file in list:
        #     if(file==filename):
        #         break
        #     else:     
        #         list=list+[filename]
        with open(filename, 'wb') as f:
            
            file_in_db=os.path.join(directory,filename)
            b_name=os.path.basename(filename)
            file_in_db=os.path.join(directory,b_name)
            
           
            f.write(requests.get(urljoin(url,link['href'])).content)
            f.close()
            

            #changes IN TITLE
            filepath=os.path.join(drive,folder,directory,b_name)
            # i=i+1
            pdf=fitz.open(filepath)
            meta=pdf.metadata          
          

            #CHANGES IN TIME
            date=meta['creationDate']
            
            if len(date)<14:
               
                f_date=date
            else:
                date=meta['creationDate'].split(':')[1]
                f_date=date[0:4]+"-"+date[4:6]+"-"+date[6:8]+" "+date[8:10]+":"+date[10:12]+":"+date[12:14]
            print("date",f_date)

            language_OF_file=language(filepath)
            # language_OF_file='NOt recognized'
            file2=files(title=file_in_db,creation_date=f_date,institution=directory,url=url,language=language_OF_file)        
          
            file2.save()
            


