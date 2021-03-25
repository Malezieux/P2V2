import module

__url__ = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

  
final_list_url = module.list_url(__url__)
listsui = module.next_url(__url__)
# i est un item de list ?
books_info_list = []
for i in final_list_url:
    #print (i)
    books_info_list.append(module.list_item(i))
  
module.final_csv(books_info_list)
    
#print (final_list_url)
print (listsui)
#print(i)
