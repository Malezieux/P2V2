import csv
from os import write
from bs4 import BeautifulSoup
import re
import requests
import pathlib


page = requests.get(
    'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
)
if page.status_code == requests.codes.ok:

    page = BeautifulSoup(page.content, 'html.parser')
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
    review_rating = (
        page.find('th', text='Number of reviews').find_next('td').text
    )
    product_description = page.find('h2').find_next('p').text
    category = page.find_all('li')[1].text
    image_url = page.find('img')['src']

with open('toto.csv', 'w', newline='') as csvfile:
    list_item = csv.writer(
        csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL
    )
    list_item.writerow(
        'title', 'upc', 'price_including_tax', 'price_excluding_tax'
    )
    list_item.writerow(title, upc, price_including_tax, price_excluding_tax)


    write