from os import write
from typing import Dict, Text
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import urllib.request
import re
import csv
from csv import DictWriter
import pathlib
from typing import Dict
import module

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
#i ='https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'

list = [module.list_url(url)]
listsui = module.next_url(url)
# i est un item de list ?
for i in list:
    module.list_item(i)
print(list)
print(listsui)
print(i)
