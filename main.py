#! /usr/bin/venv python3
# coding: utf-8

import module
import os

os.makedirs('images')
url_first = 'https://books.toscrape.com/'
category_urls = module.category_url(url_first)

list_book_page = module.category_urls_next(category_urls)


item_book = []
for _ in list_book_page:
    item_book.append(module.list_item_by_book(_))
    module.final_csv(item_book)
