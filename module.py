
import requests
from bs4 import BeautifulSoup
import re
import urllib
from csv import DictWriter


# select all url book by page
def list_url(url):
    page = requests.get(
        url
        )
    if page.status_code == requests.codes.ok:
        page = BeautifulSoup(page.content, 'html.parser')
    list_url_page = []
    for div in page.select('h3 a'):
        list_url_page.append('https://books.toscrape.com/catalogue/'+(div.get('href'))[6:])
    return list_url_page

# select url neext page for liste_url
def next_url(url):
    page = requests.get(
        url
        )
    if page.status_code == requests.codes.ok:
            page = BeautifulSoup(page.content, 'html.parser')
    url_suite = url[0:-10] + page.find('a', text='next').get('href')
    return url_suite

# select all item by book
def list_item (i):

        page = requests.get(i)
        if page.status_code == requests.codes.ok:
            page = BeautifulSoup(page.content, 'html.parser')


        product_page_url = i
        title = page.find('h1').text
        upc = page.find('th', text='UPC').find_next('td').text
        price_including_tax = (
            page.find('th', text='Price (incl. tax)').find_next('td').text
        )
        price_excluding_tax = (
            page.find('th', text='Price (excl. tax)').find_next('td').text
        )
        number_available_before = (
            page.find('th', text='Availability').find_next('td').text
        )
        number_available = int(re.search('\d+', number_available_before).group(0))
        review_rating = (
            page.find('th', text='Number of reviews').find_next('td').text
        )
        product_description = (
            page.find('h2').find_next('p').text
        )  
        category = page.find_all('li')[1].text
        image_url = page.find('img')['src']

        image = urllib.request.urlretrieve('https://books.toscrape.com/'+ image_url[6:0], upc +'.jpg')
        data = {'product_page_url':product_page_url,'title':title,'upc':upc,'price_including_tax':price_including_tax,'price_excluding_tax':price_excluding_tax,'number_available':number_available,'review_rating':review_rating,'product_description':product_description,'category':category,'image_url':image_url}
        
        # fonction final_csv create csv 
        return data



#export csv
def final_csv(data):
    with open('test.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames=['product_page_url','title', 'upc', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'product_description', 'category', 'image_url']
        list_item_csv = DictWriter(csvfile, delimiter='|', fieldnames=fieldnames, quotechar='|')
    #for item in data:
        list_item_csv.writeheader()
    
        for item in data:
            list_item_csv.writerow (item)
        print(data)
