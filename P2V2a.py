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
url= '(module.page_catalogue(5))'
#url='https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'

page = requests.get(url)
if page.status_code == requests.codes.ok:
    page = BeautifulSoup(page.content, 'html.parser')


    product_page_url = module.page_catalogue
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
    review_rating = (
        page.find('th', text='Number of reviews').find_next('td').text
    )
    product_description = (
        page.find('h2').find_next('p').text
    )  
    category = page.find_all('li')[1].text
    image_url = page.find('img')['src']

    image = urllib.request.urlretrieve('https://books.toscrape.com/'+ image_url[6:0], upc +'.jpg')
    data = {'product_page_url':product_page_url,'title':title,'upc':upc,'price_including_tax':price_including_tax,'price_excluding_tax':price_excluding_tax,'number_available':number_available,'review_rating':review_rating,'product_description':product_description,'category':category,'image_url':image_url}
    
    # fonction final_csv create csv 
    module.final_csv(data) 