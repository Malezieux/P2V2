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

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

list = module.list_item(url)
listsui = module.next_url(url)
print(list)
print(listsui)
