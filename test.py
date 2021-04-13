
import module

url_first = 'https://books.toscrape.com/index.html'
erotica_50 ='https://books.toscrape.com/catalogue/category/books/erotica_50/index.html'		
crime_51 ='https://books.toscrape.com/catalogue/category/books/romance_8/index.html'


dico_categorie = {
'Erotica' : erotica_50,
'Crime' : crime_51,
}

url_book = []
items_book = []
ask_category = (input(f'What category you want ?{dico_categorie.keys}'))
for ask_category in dico_categorie:
    url_book.append(module.list_url_book_by_page(dico_categorie[ask_category]))
    for url in url_book:
        items_book.append(module.list_item_by_book(url))
    print(items_book)