from django.shortcuts import render
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from news.models import files
from django.core.files import File
from urllib.parse import urlparse
import fitz
from urllib3.exceptions import NewConnectionError
from langdetect import detect


import PyPDF2
list = []

# urls = ['http://mohp.gov.np/', 'http://nepalindata.com/resource/category/laws-policies-and-strategies/', 'http://nepalconsular.gov.np/np/',
#         'http://www.dotm.gov.np/', 'http://mofa.gov.np/', 'http://www.dop.gov.np/', 'http://ciaa.gov.np/', "https://mod.gov.np/",
#         "http://moe.gov.np/",      "https://mohp.gov.np/en",      "https://www.moud.gov.np/",        "https://moys.gov.np/",     "https://www.nepal.gov.np/",
#         "http://www.mopit.gov.np/",        "https://www.mof.gov.np/",     "https://www.moald.gov.np/",        "http://www.ntc.net.np/",        "http://www.nitc.gov.np/",         "http://www.nepalairlines.com.np",        "http://www.cca.gov.np/"]


urls = ['http://mohp.gov.np/',  'http://nepalconsular.gov.np/np/',
        'http://www.dotm.gov.np/', 'http://mofa.gov.np/',

        ]

# urls=['https://docs.flutter.dev/get-started/install/windows']


def date(filepath):
    try:
        pdf = fitz.open(filepath)
        meta = pdf.metadata
        date = meta['creationDate']
        if len(date) < 14:
            f_date = date
        else:
            date = meta['creationDate'].split(':')[1]
            f_date = date[0:4]+"-"+date[4:6]+"-"+date[6:8] + \
                " "+date[8:10]+":"+date[10:12]+":"+date[12:14]
        return f_date

    except (RuntimeError, TypeError, NameError, KeyError, IndexError, AttributeError) as e:
        pass


def language(texts):
    special_characters = "!@#$%^&*()-+?_=,<>/[]{}|\~`"
    j = 0
    n_count = 0
    e_count = 0
    try:
        text = texts.split(' ')
        # print(text)
        for txt in text:
            txt = text[j]
            if any(c in special_characters for c in txt) or txt.isnumeric() == True:
                # print(txt)

                j = j+1

                continue
            else:
                if(len(txt) >= 3):
                    # print(txt)
                    if (detect(txt) == 'ne' or detect(txt) == 'hi'):
                        n_count = n_count+1
                    else:
                        e_count = e_count+1
            j = j+1
        # print("Nepali:", n_count)
        # print("English:" ,e_count)
        if(n_count > e_count):
            return "Nepali"
        else:
            return "English"
    except:
        pass


for url in urls:
    drive = 'D:\\'
    folder = 'data'
    urlparse(url)
    folders = urlparse(url).netloc
    if(folders.split('.')[0] == 'www'):
        directory = folders.split('.')[1]
    else:
        directory = folders.split('.')[0]
    folder_location = os.path.join(drive, folder, directory)
    if not os.path.exists(folder_location):
        os.mkdir(folder_location)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for title in soup.find_all('title'):
            title_name = title.get_text()
    except (requests.exceptions.SSLError, requests.exceptions.ConnectionError, NewConnectionError) as e:
        pass
    i = 0

    def pdf():
        for link in soup.select("a[href$='.pdf']"):
            print(directory)
            a_title = link.parent.contents[0].text
            a_link = link.get('href')

            print(a_title)
            # print(link['href'])

            file_actual = os.path.join(folder_location, link['href'])
            filename = os.path.join(
                folder_location, link['href'].split('/')[-1])
            print(file_actual)
            try:
                department = soup.find('title').text
                print(department)
            except AttributeError:
                department = ''

            # pdfFileObj = open(filename, 'rb')
            # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # print(pdfReader.numPages)
            # for i in range(pdfReader.numPages):
            #     pageObj = pdfReader.getPage(i)
            #     print(pageObj.extractText())

            try:
                with open(filename, 'wb') as f:
                    print(directory)

                    file_in_db = os.path.join(directory, filename)
                    b_name = os.path.basename(filename)
                    file_in_db = os.path.join(directory, b_name)

                    f.write(requests.get(urljoin(url, link['href'])).content)
                    f.close()

                    # changes IN TITLE
                    filepath = os.path.join(drive, folder, directory, b_name)
                    # i=i+1
                    f_date = date(filepath)

                    # language_OF_file=language(filepath)
                    language_OF_file = language(a_title)
                    # print(language_OF_file)
                    file2 = files(title=a_title, fullfile=file_in_db, creation_date=f_date,
                                  institution=department, url=a_link, language=language_OF_file)

                    file2.save()

            except (requests.exceptions.Timeout, FileNotFoundError, OSError) as e:
                pass

    def zip():
        for link in soup.select("a[href$='.zip']"):
            print(directory)
            a_title = link.parent.contents[0].text
            a_link = link.get('href')
            print(a_link)
            print(a_title)
            # print(link['href'])

            file_actual = os.path.join(folder_location, link['href'])
            filename = os.path.join(
                folder_location, link['href'].split('/')[-1])
            print(file_actual)
            try:
                department = soup.find('title').text
                print(department)
            except AttributeError:
                department = ''

            #  tag=soup.find_all("div", {"class": "text"})[i]
            #  print(" ")
            #  print(tag.find('a').contents)
            # except AttributeError:
            #     pass
            # i=i+1
            try:
                with open(filename, 'wb') as f:
                    print(directory)

                    file_in_db = os.path.join(directory, filename)
                    b_name = os.path.basename(filename)
                    file_in_db = os.path.join(directory, b_name)

                    f.write(requests.get(urljoin(url, link['href'])).content)
                    f.close()

                    # changes IN TITLE
                    filepath = os.path.join(drive, folder, directory, b_name)
                    # i=i+1
                    f_date = date(filepath)

                    # language_OF_file=language(filepath)
                    language_OF_file = language(a_title)
                    # print(language_OF_file)
                    file2 = files(title=a_title, fullfile=file_in_db, creation_date=f_date,
                                  institution=department, url=a_link, language=language_OF_file)

                    file2.save()

            except (requests.exceptions.Timeout, FileNotFoundError) as e:
                pass

    def pptx():
        for link in soup.select("a[href$='.pptx']" or "a[href$='.xlsx']" or "a[href$='.docx']" or "a[href$='.txt']"):
            print(directory)
            a_title = link.parent.contents[0].text
            a_link = link.get('href')
            print(a_link)
            print(a_title)
            # print(link['href'])

            file_actual = os.path.join(folder_location, link['href'])
            filename = os.path.join(
                folder_location, link['href'].split('/')[-1])
            print(file_actual)
            try:
                department = soup.find('title').text
                print(department)
            except AttributeError:
                department = ''

            try:
                with open(filename, 'wb') as f:
                    print(directory)

                    file_in_db = os.path.join(directory, filename)
                    b_name = os.path.basename(filename)
                    file_in_db = os.path.join(directory, b_name)

                    f.write(requests.get(urljoin(url, link['href'])).content)
                    f.close()

                    # changes IN TITLE
                    filepath = os.path.join(drive, folder, directory, b_name)
                    # i=i+1
                    f_date = date(filepath)

                    # language_OF_file=language(filepath)
                    language_OF_file = language(a_title)
                    # print(language_OF_file)
                    file2 = files(title=a_title, fullfile=file_in_db, creation_date=f_date,
                                  institution=department, url=a_link, language=language_OF_file)

                    file2.save()

            except (requests.exceptions.Timeout, FileNotFoundError) as e:
                pass

    def image():
        try:
            for link in soup.select("img[src]"):
                print(directory)
                a_title = link.parent.contents[0].text
                a_link = link.get('src')
                print(a_link)
                print(a_title)
                # print(link['href'])

                file_actual = os.path.join(folder_location, link['src'])
                filename = os.path.join(
                    folder_location, link['src'].split('/')[-1])
                print(file_actual)
                try:
                    department = soup.find('title').text
                    print(department)
                except AttributeError:
                    department = ''
                try:
                    with open(filename, 'wb') as f:
                        print(directory)

                        file_in_db = os.path.join(directory, filename)
                        b_name = os.path.basename(filename)
                        file_in_db = os.path.join(directory, b_name)

                        f.write(requests.get(
                            urljoin(url, link['src'])).content)
                        f.close()

                        # changes IN TITLE
                        filepath = os.path.join(
                            drive, folder, directory, b_name)
                        # i=i+1
                        f_date = date(filepath)

                        # language_OF_file=language(filepath)
                        language_OF_file = language(a_title)
                        # print(language_OF_file)
                        file2 = files(title=a_title, fullfile=file_in_db, creation_date=f_date,
                                      institution=department, url=a_link, language=language_OF_file)

                        file2.save()

                except (requests.exceptions.Timeout, FileNotFoundError, OSError) as e:
                    pass
        except FileNotFoundError:
            pass
    pdf()
    zip()
    pptx()
    image()


def search(request):
    user_list = files.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, {'filter': user_filter})
