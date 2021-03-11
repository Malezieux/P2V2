from os import write
from re import findall, search
import re
from typing import Text
from urllib.request import url2pathname
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import re
import csv
from csv import DictWriter
import pathlib
import module

#liste de toute les pages


numero = (1,2,3,2,4)   


while 2 in numero:
    page = requests.get(
    module.page_catalogue(numero)
)
if page.status_code == requests.codes.ok:

    page = BeautifulSoup(page.content, 'html.parser')

for div in page.select('h3 a'):
    list_url= (div.get('href'))[6:]
    print(list_url)



