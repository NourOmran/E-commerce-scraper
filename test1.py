
import urllib.request
import ssl
import requests
from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

ssl._create_default_https_context = ssl._create_unverified_context

def parse_ul(elem):
    result = {}
    for sub in elem.find_all('li', recursive=False):
        if sub.a is None:
            continue
        data = {k: v for k, v in sub.a.attrs.items() if k != 'class'}
        if sub.ul is not None:
            # recurse down
            data['children'] = parse_ul(sub.ul)
        result[sub.a.get_text(strip=True)] = data
    return result


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.ulta.com/search?search=mango+butter+")
driver.implicitly_wait(20)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)
ul      = parse_ul(soup.ul)

print(len(ul))