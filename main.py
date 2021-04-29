#! /usr/bin/venv python3
# coding: utf-8
from module import *

url_first = 'https://books.toscrape.com/'
url_category = category(url_first)
url_next_category = []
for url in url_category[2:6]:
    if next_url := next_url_page(url):
        url_next_category = next_url_page(url)
all_url_category = url_category + url_next_category
url_book = []
for a in all_url_category:
    url_book.append(list_url_book_by_page(a))
print(all_url_category)
print(url_book)
