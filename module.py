import requests
from bs4 import BeautifulSoup
from csv import DictWriter




def list_item(url):
    page = requests.get(
        url
        )
    if page.status_code == requests.codes.ok:
            page = BeautifulSoup(page.content, 'html.parser')
    for div in page.select('h3 a'):
            list_url= 'https://books.toscrape.com/catalogue/'+(div.get('href'))[6:]
            print (list_url)


def next_url(url):
    page = requests.get(
        url
        )
    if page.status_code == requests.codes.ok:
            page = BeautifulSoup(page.content, 'html.parser')
    url_suite = url[0:-10] + page.find('a', text='next').get('href')
    return(url_suite)
        




def final_csv(data):
    with open('testh.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames=['product_page_url','title', 'upc', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'product_description', 'category', 'image_url']
        list_item = DictWriter(csvfile, delimiter='|', fieldnames=fieldnames, quotechar='|')
    #for item in data:
        list_item.writeheader()
    
        list_item.writerow(data)
        print(data)
