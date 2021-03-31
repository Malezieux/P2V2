import module
#url de depart
url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'


#url de la page suivant, un seul résultat a chaque fois !!!
next_url = module.next_url_page(url)

#liste des url de chaque page
final_list_url = module.list_url_book_by_page(url)

#dictionnaire des infos de chaque livre issus 
books_info_list = []
for i in final_list_url:
        #print (i)
        books_info_list.append(module.list_item_by_book(i))

#export en csv du résultat   
module.final_csv(books_info_list)
    
print (final_list_url)
#print (url)
print(next_url)
