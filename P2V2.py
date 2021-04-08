from bs4 import BeautifulSoup
from module import category
import module
#url de depart
url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
url3 = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
url2 = 'https://books.toscrape.com/index.html'

url_category = module.category(url2)
url_book = []
for a in url_category:
    url_book.append(a)
    ul = []
    for i in url_book:
        ul.append(module.list_url_book_by_page(i))
    
print (url_book)
f = open("test.txt", "w")
print(f.readline(ul))
f.close() 