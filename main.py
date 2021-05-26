#! /usr/bin/venv python3
# coding: utf-8

import booktoscrap
import os

os.makedirs('images')
url_first = 'https://books.toscrape.com/'
category_urls = booktoscrap.category_url(url_first)

list_book_page = booktoscrap.category_urls_next(category_urls)


item_book = []
for _ in list_book_page:
    item_book.append(booktoscrap.list_item_by_book(_))
    booktoscrap.final_csv(item_book)
