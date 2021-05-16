#! /usr/bin/venv python3
# coding: utf-8
from module import *


url_first = 'https://books.toscrape.com/'
<<<<<<< HEAD
url_category = category(url_first)

print(url_category)

=======
page = requests.get(url_first)
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.content, 'html.parser')
    side_categories = soup.find('div', class_='side_categories')
    category_urls = []
    for _ in side_categories.find_all('a')[1:6]:
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

    for _ in category_urls_next:
        i = 5
        urlnext = _[:-11]
        urlz = f'{urlnext}page-{i}.html'
        # page = requests.get(toto)
        # if page.status_code == requests.codes.ok:
        print(urlz)

print(category_urls, category_urls_next)


# print(url_book)
>>>>>>> 3b17cee (test boucle)
