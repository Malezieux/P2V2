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

page = requests.get(
    'http://books.toscrape.com/catalogue/soumission_998/index.html'
)
if page.status_code == requests.codes.ok:

    page = BeautifulSoup(page.content, 'html.parser')