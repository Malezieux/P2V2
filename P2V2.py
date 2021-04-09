from bs4 import BeautifulSoup
from module import category
import module
#url de depart
url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
url3 = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
url2 = 'https://books.toscrape.com/index.html'

url_category = module.category(url2)
url_book = []
items_book = []
ul = []

for a in url_category:
    url_book.append(module.list_url_book_by_page(a))
for i in url_book[1]:
    ul.append(module.list_item_by_book(i))

module.final_csv(ul)

#for i in url_book:
#ul.append(module.list_url_book_by_page(i))
    
#for z in ul:
#items_book.append(module.list_item_by_book(z))
#print (a)
print (url_category)
#print (url_book)
#print (items_book)  

#print (ul)
