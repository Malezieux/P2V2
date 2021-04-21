from bs4 import BeautifulSoup
from module import category, list_url_book_by_page
import module
import requests

# url de depart

url_first = 'https://books.toscrape.com/'
url_category = module.category(url_first)
print(url_category)


