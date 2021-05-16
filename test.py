from module import next_url_page
from bs4 import BeautifulSoup
import requests


page = requests.get('https://books.toscrape.com')
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.content, 'html.parser')
    side_categories = soup.find('div', class_='side_categories')
    category_urls = []
    for a in side_categories.find_all('a')[1:6]:
        category_urls.append('https://books.toscrape.com/' + a.get('href'))
        for url in category_urls:
                toto = next_url_page(url)
print(category_urls, toto)

def next_url_page(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        soup = BeautifulSoup(page.content, 'html.parser')
        # for text_next in soup:
        next_url = []
        if soup.find('a', text='next'):
            next_url.append(url.replace('index.html', 'page-2.html'))
        else:
            pass

    return next_url