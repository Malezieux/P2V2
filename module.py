import requests
from bs4 import BeautifulSoup
from csv import DictWriter

# list les url 
def page_catalogue(numero):

    page_num = (numero + 1)
    my_url = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'.format(page_num)
    return my_url



def final_csv(data):
    with open('testh.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames=['product_page_url','title', 'upc', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'product_description', 'category', 'image_url']
        list_item = DictWriter(csvfile, delimiter='|', fieldnames=fieldnames, quotechar='|')
    #for item in data:
        list_item.writeheader()
    
        list_item.writerow(data)
        print(data)
