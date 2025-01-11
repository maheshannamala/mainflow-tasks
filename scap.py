import requests 
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Main_Page"
response=requests.get(url)
if response.status_code==200:
   soup=BeautifulSoup(response.text,"html.parser")
   p_text=soup.get_text()
   links=[a['href'] for a in soup.find_all('a',href=True)]
   images=[img['src'] for img in soup.find_all('img',src=True)]
   print("page text :",p_text)
   print("\nlinks:")
   for l in links:
      print(l)
   print("\n images")
   for img in images:
      print(img)
else:
   print("error")
