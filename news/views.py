from django.shortcuts import render
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from news.models import files
from django.core.files import File

urls=['https://nepalindata.com/resource/category/laws-policies-and-strategies/','http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html','https://nepalconsular.gov.np/np/','https://www.dotm.gov.np/','https://mofa.gov.np/','https://merolagani.com/','https://www.dop.gov.np/','http://ciaa.gov.np/','https://mohp.gov.np/']
# urls=['http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html']
i=0
for url in urls:
    i=i+1
    drive='D:'
    folder='nid'
    directory='web'+str(i)
    # folder_location = r'D:\\nid\web'+str(i)
    folder_location = os.path.join(drive,folder,directory)
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")     

    for link in soup.select("a[href$='.pdf']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            file_in_db=os.path.basename(filename)
            f.write(requests.get(urljoin(url,link['href'])).content)
            f.close()
            # path='D:\\nid\web'+str(i)+'\\'+filename
        
            filepath=os.path.join(drive,folder,directory,file_in_db)
            file2=open(filepath, 'rb')
            file2=files(title=file_in_db)
            file2.save()
          



