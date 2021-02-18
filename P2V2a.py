from os import write
from re import findall, search
import re
from sys import modules
from typing import Text
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import re
import csv
from csv import DictWriter
import pathlib
import module


page = module.page
product_page_url = 'test'
title = page.find('h1').text
upc = page.find('th', text='UPC').find_next('td').text
price_including_tax = (
    page.find('th', text='Price (incl. tax)').find_next('td').text
)
price_excluding_tax = (
    page.find('th', text='Price (excl. tax)').find_next('td').text
)
number_available_before = (
    page.find('th', text='Availability').find_next('td').text
)
number_available = int(re.search('\d+', number_available_before).group(0))
review_rating = page.find('th', text='Number of reviews').find_next('td').text
product_description = (
    page.find('h2').find_next('p').text
)  # mettre triple quillemets
category = page.find_all('li')[1].text
image_url = page.find('img')['src']
f = (
    product_page_url,
    title,
    upc,
    price_including_tax,
    price_excluding_tax,
    number_available,
    review_rating,
    product_description,
    category,
    image_url,
)
print(f)
with open('test.csv', 'w', newline='') as csvfile:

    list_item = csv.writer(csvfile, delimiter=' ', quotechar='|')
    list_item.writerows(
        ('title', 'upc', 'price_including_tax', 'price_excluding_tax')
    )

    list_item.writerows([f])
