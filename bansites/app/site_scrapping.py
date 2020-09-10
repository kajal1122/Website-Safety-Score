from bs4 import BeautifulSoup
import urllib.request , urllib.parse, urllib.error


# lets just get input and perform function


url = "https://www.flipkart.com"

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
body = soup.find('body').get_text()
for b in body:
    print(b)
