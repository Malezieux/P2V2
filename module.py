import requests
from bs4 import BeautifulSoup
from csv import DictWriter

#url= 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
def final_csv(mydata):
    with open('testh.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames=['product_page_url','title', 'upc', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'product_description', 'category', 'image_url']
        list_item = DictWriter(csvfile, delimiter='|', fieldnames=fieldnames, quotechar='|')
    #for item in data:
        list_item.writeheader()
    
        list_item.writerow(mydata)
        print(mydata)
