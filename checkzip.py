from bs4 import BeautifulSoup
import requests

response= requests.get("https://www.dop.gov.np")
soup= BeautifulSoup(response.text, "html.parser")

image=soup.find('img')
img_url=image['src']
print(img_url)
print(image)
image=requests.get('img_url')
# for link in soup.s
# elect(image):
with open('image.jpg', 'wb') as file:
      for chunk in image.iter_content(chunk_size=1024):
        file.write(chunk)
       
   

# url=['https://docs.flutter.dev/get-started/install/windows']
# ppt = requests.get('http://www.howtowebscrape.com/examples/media/images/SampleSlides.pptx')


# with open('sample.pptx', 'wb') as file:
#     for chunk in ppt.iter_content(chunk_size=1024):
#         file.write(chunk)