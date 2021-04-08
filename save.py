import requests
from bs4 import BeautifulSoup
import re
import urllib
from csv import DictWriter


url3 = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
page = requests.get(url3)
page.raise_for_status()
soup = BeautifulSoup(page.content, 'html.parser')    
upc = page.find('th', text='UPC').find_next('td').text
print (upc)

def category (url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        page = BeautifulSoup(page.content, 'html.parser')
        list_url_page = []

        side_categories = page.find('div', class_='side_categories')
        for li in side_categories.find_all('a'):
            list_url_page.append(
            (li.get('href'))
        )
        return (list_url_page)
