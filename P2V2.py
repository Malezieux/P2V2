from os import write
from re import findall, search
import re
from typing import Text
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import re
import csv
from csv import DictWriter
import pathlib
import module

#liste de toute les pages

numero=3
page = requests.get(
    module.page_catalogue(numero)
)
if page.status_code == requests.codes.ok:

    page = BeautifulSoup(page.content, 'html.parser')

for div in page.select('h3 a'):
    list_url= (div.get('href'))[6:]
    print(list_url)

print (module.page_catalogue(25))

