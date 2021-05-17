#! /usr/bin/venv python3
# coding: utf-8
from module import *


url_first = 'https://books.toscrape.com/'

page = requests.get(url_first)
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.content, 'html.parser')
    side_categories = soup.find('div', class_='side_categories')
    category_urls = []
    for _ in side_categories.find_all('a')[1:]:
        category_urls.append('https://books.toscrape.com/' + _.get('href'))
    category_urls_next = []
    for _ in category_urls:
        page = requests.get(_)
        if page.status_code == requests.codes.ok:
            soup = BeautifulSoup(page.content, 'html.parser')
            if soup.find('a', text='next'):
                category_urls_next.append(
                    _.replace('index.html', 'page-2.html')
                )
    resturl = []
    for _ in category_urls_next:
        i = [3, 4, 5, 6, 7]
        urlnext = _[:-11]

        for _ in i:
            urlz = f'{urlnext}page-{_}.html'
            page = requests.get(urlz)
            if page.status_code == requests.codes.ok:
                resturl.append(urlz)
            else:
                pass
category_urls.extend(category_urls_next + resturl)
print(category_urls)


# print(url_book)
