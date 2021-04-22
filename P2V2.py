from bs4 import BeautifulSoup
from module import category, list_url_book_by_page
import requests

# Récupere toutes les url de la 1ere page de chaque categorie
def category(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        soup = BeautifulSoup(page.content, 'html.parser')
        side_categories = soup.find('div', class_='side_categories')
        category_urls = []
        for a in side_categories.find_all('a'):
            category_urls.append('https://books.toscrape.com/' + a.get('href'))
        return category_urls


#
def next_url_page(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        page = BeautifulSoup(page.content, 'html.parser')
        a = url
        
        if page.find_all('a', text='next'):
            next_url = url.replace('index.html', 'page-1.html')
    
            return next_url

def next_url_page_s(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        page = BeautifulSoup(page.content, 'html.parser')
        a = url
        next_url_s = []
        i = 1
        if page.find('a', text='next'):
            i += 1
        next_url_s.append(url.replace('page-' + str(i - 1) + '.html','page-' + str(i) + '.html',))
    else:
        pass
    return next_url_s

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



url_first = 'https://books.toscrape.com/'
url_category = category(url_first)
url_next_category = []
url_next_category_suite = []
for url in url_category[2:7]:
    url_next_category.append(next_url_page(url))
    for url in url_next_category:
        url_next_category_suite.append(next_url_page_s(url))
    print(url_next_category_suite)


