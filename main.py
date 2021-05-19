#! /usr/bin/venv python3
# coding: utf-8
import module
import requests
from bs4 import BeautifulSoup


url_first = 'https://books.toscrape.com/'
page = requests.get(url_first)
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.content, 'html.parser')
    side_categories = soup.find('div', class_='side_categories')
    category_urls = []
    for _ in side_categories.find_all('a')[1:]:
        category_urls.append('https://books.toscrape.com/' + _.get('href'))

    category_next_urls = []
    list_book_page = []
    for _ in category_urls:
        page = requests.get(_)
        if page.status_code == requests.codes.ok:
            category_next_urls.append(_)
            soup = BeautifulSoup(page.content, 'html.parser')
            for div in soup.select('h3 a'):
                list_book_page.append(
                    'https://books.toscrape.com/catalogue/'
                    + (div.get('href')[9:])
                )
    for _ in category_urls:
        url = _[:-10]
        i = [2, 3, 4, 5, 6, 7, 8]
        for _ in i:
            urlnext = f'{url}page-{_}.html'
            page = requests.get(urlnext)
            if page.status_code == requests.codes.ok:
                category_next_urls.append(urlnext)
                soup = BeautifulSoup(page.content, 'html.parser')
                for div in soup.select('h3 a'):
                    list_book_page.append(
                        'https://books.toscrape.com/catalogue/'
                        + (div.get('href')[9:])
                    )
            else:
                pass
item_book = []
for _ in list_book_page:
    item_book.append(module.list_item_by_book(_))
    module.final_csv(item_book)
print(item_book)

# print(url_book)
