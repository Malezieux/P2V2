from bs4 import BeautifulSoup
from module import category
import module
#url de depart

url_first = 'https://books.toscrape.com/index.html'

url_category = module.category(url_first)
url_book = []
items_book = []

for url in url_category[1:]:
    url_book = module.list_url_book_by_page (url)
    for url in url_book:
        items_book.append(module.list_item_by_book(url))

module.final_csv(items_book)

print (url_category)
print (len(url_book))
print (items_book)  
