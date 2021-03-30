import module

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

list_next_url = module.next_url(url)


final_list_url =[]
final_list_url = module.list_url(list_next_url)
# i est un item de list ?
books_info_list = []
for i in final_list_url:
        #print (i)
        books_info_list.append(module.list_item(i))
  
module.final_csv(books_info_list)
    
print (final_list_url)
#print (url)
print(list_next_url)
