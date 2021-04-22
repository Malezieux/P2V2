import requests
from bs4 import BeautifulSoup
import re
import urllib.request
from csv import DictWriter


# select all url category
def category(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        soup = BeautifulSoup(page.content, 'html.parser')
        category_urls = []
        side_categories = soup.find('div', class_='side_categories')
        for a in side_categories.find_all('a'):
            category_urls.append('https://books.toscrape.com/' + a.get('href'))
            
            
            for lien in category_urls[1:]:
                response = requests.get(lien)
                if response.ok:
                    lien = lien.replace('index.html', 'page-1.html')
                    r = requests.get(lien)
                    if r.ok:
                        i = 1
                        url_cat = []
                        url_cat.append(lien)
                        while r.ok:
                            i += 1
                            url_cat_next = []
                            lien = lien.replace('page-' + str(i - 1) + '.html','page-' + str(i) + '.html',)
                            r = requests.get(lien) 
                            if r.ok:
                            
                                url_cat_next.append(lien)
                                pass
                
        return (url_cat, url_cat_next)


# select all url book by page
def list_url_book_by_page(url):
    page = requests.get(url)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, 'html.parser')
    list_url_page = []
    
    for div in soup.select('h3 a'):
        list_url_page.append(
            'https://books.toscrape.com/catalogue/' + (div.get('href'))
        )
    return list_url_page


# select url next page
def next_url_page(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        page = BeautifulSoup(page.content, 'html.parser')
        a = url[:-10]
        if page.find('a', text='next'):
            next_url = a + ('page-2.html')
        return next_url


# select all item by book
def list_item_by_book(url):
    page = requests.get(url)
    page.raise_for_status()
    page = BeautifulSoup(page.content, 'html.parser')

    product_page_url = url
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
    product_description = page.find('h2').find_next('p').text
    category = page.find_all('li')[2].text[1:-1]
    image_url = 'images/' + upc + '.jpg'
    image_url_source = page.find('img')['src']
    rep_image = 'C:/Travail/03 Formations/P2V2/images/' + upc + '.jpg'
    image = urllib.request.urlretrieve(
        'https://books.toscrape.com/' + image_url_source[6:], rep_image
    )
    data = {
        'product_page_url': product_page_url,
        'title': title,
        'upc': upc,
        'price_including_tax': price_including_tax,
        'price_excluding_tax': price_excluding_tax,
        'number_available': number_available,
        'review_rating': review_rating,
        'product_description': product_description,
        'category': category,
        'image_url': image_url,
    }

    # fonction final_csv create csv
    return data


# export csv
def final_csv(data):
    with open('test.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames = [
            'product_page_url',
            'title',
            'upc',
            'price_including_tax',
            'price_excluding_tax',
            'number_available',
            'review_rating',
            'product_description',
            'category',
            'image_url',
        ]
        list_item_csv = DictWriter(
            csvfile,
            delimiter='|',
            fieldnames=fieldnames,
        )
        # for item in data:
        list_item_csv.writeheader()

        for item in data:
            list_item_csv.writerow(item)
        print(data)
