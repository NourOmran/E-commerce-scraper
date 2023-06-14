
import urllib.request
import ssl
import requests
from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

ssl._create_default_https_context = ssl._create_unverified_context

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.ulta.com/search?search=mango+butter+")
time.sleep( 5 )
html = driver.page_source

#response = requests.get("https://www.ulta.com/search?search=mango+butter+")
#print(response.content)
soup = BeautifulSoup(html, 'html.parser')

href = soup.find_all("a") # Find all elements with the tag <a>
links = []
for link in href:
    if is_url(link.get("href")):
        links.append(link.get("href"))
counter = 0
print(len(links))
for link in links:
    if requests.get(link).ok:
        webpage = str(urllib.request.urlopen(link).read())
        soup = BeautifulSoup(webpage)

        page_txt = soup.get_text()

        txts = [ ]
        if "Mangifera Indica (Mango) Seed Butter" in page_txt :
            counter = counter +1
            txts.append(str(page_txt))
            text_file = open(f"sample{counter}.txt", "wt")
            n = text_file.write(str(page_txt))
            text_file.close()
            print(counter)
        if counter == 3:
            break
