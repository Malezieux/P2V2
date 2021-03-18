import module

__url__ = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
#i ='https://books.toscrape.com/catalogue/
# scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'

final_list_url = [module.list_url(__url__)]
listsui = module.next_url(__url__)
# i est un item de list ?
for i in final_list_url:
    module.list_item(i)
print (final_list_url)

print(i)
