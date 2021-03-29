import module

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

  
final_list_url = (module.next_url(url))
# i est un item de list ?
books_info_list = []
u=[]
while u in final_list_url:# tant que url_suit
    for i in final_list_url:
        #print (i)
        books_info_list.append(module.list_item(i))
        url = module.next_url(url)
  
module.final_csv(books_info_list)
    
#print (final_list_url)
print (url)
#print(i)
