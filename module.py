import requests
from bs4 import BeautifulSoup
import urllib.request
from csv import DictWriter
from bs4 import BeautifulSoup
import re

# select all category
def category_url(url_first):
    page = requests.get(url_first)
    if page.status_code == requests.codes.ok:
        soup = BeautifulSoup(page.content, 'html.parser')
        side_categories = soup.find('div', class_='side_categories')
        category_urls = []
        for _ in side_categories.find_all('a')[1:2]:
            category_urls.append('https://books.toscrape.com/' + _.get('href'))
        return category_urls
    print(category_urls)


# select all url book by category
def category_urls_next(category_urls):
    category_next_urls = []
    list_book_page = []
    for _ in category_urls:
        page = requests.get(_)
        if page.status_code == requests.codes.ok:
            category_next_urls.append(_)
            soup = BeautifulSoup(page.content, 'html.parser')
            for div in soup.select('h3 a'):
                list_book_page.append(
                    'https://books.toscrape.com/catalogue/'
                    + (div.get('href')[9:])
                )
        url = _[:-10]
        next_page = True
        last_page = 1
        while next_page:
            last_page += 1
            urlnext = f'{url}page-{last_page}.html'
            try:
                page = requests.get(urlnext)
                page.raise_for_status()
            except requests.HTTPError:
                next_page = False
            else:
                if page.status_code == requests.codes.ok:
                    category_next_urls.append(urlnext)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    for div in soup.select('h3 a'):
                        list_book_page.append(
                            'https://books.toscrape.com/catalogue/'
                            + (div.get('href')[9:])
                        )
                else:
                    pass
    return list_book_page


# select all item by book
def list_item_by_book(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
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
        number_available = int(
            re.search('\d+', number_available_before).group(0)
        )
        review_rating = (
            page.find('th', text='Number of reviews').find_next('td').text
        )
        product_description = page.find('h2').find_next('p').text
        category = page.find_all('li')[2].text[1:-1]
        image_url = page.find('img')['src']
        rep_image = 'images/' + upc + '.jpg'
        image = urllib.request.urlretrieve(
            'https://books.toscrape.com/' + image_url[6:], rep_image
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
            'url_image': rep_image,
        }
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
            'url_image',
        ]
        list_item_csv = DictWriter(
            csvfile,
            delimiter='|',
            fieldnames=fieldnames,
        )
        # for item in data:
        list_item_csv.writeheader()
        for _ in data:
            list_item_csv.writerow(_)
    print(data)
