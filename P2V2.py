from bs4 import BeautifulSoup
from module import category
import module
#url de depart
url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
url3 = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
url2 = 'https://books.toscrape.com/index.html'

url_category = module.category(url2)
url_book = []
ul = []
items_book = []
for a in url_category:
    url_book.append(a)

    for i in url_book:
        ul.append(module.list_url_book_by_page(i))
        for a in ul:
            items_book.append(module.list_item_by_book(a))

print (items_book)  

#print (ul)
