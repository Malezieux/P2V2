from sys import modules
import requests
from bs4 import BeautifulSoup
import re
import urllib
from csv import DictWriter
import module



books_1 ='https://books.toscrape.com/catalogue/category/books_1/index.html'		
travel_2 ='https://books.toscrape.com/catalogue/category/books/travel_2/index.html'		
mystery_3 ='https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'		
historical_fiction_4 ='https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'		
sequential_art_5 ='https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'		
classics_6 ='https://books.toscrape.com/catalogue/category/books/classics_6/index.html'		
philosophy_7 ='https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html'		
romance_8 ='https://books.toscrape.com/catalogue/category/books/romance_8/index.html'		
womens_fiction_9 ='https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html'		
fiction_10 ='https://books.toscrape.com/catalogue/category/books/fiction_10/index.html'		
childrens_11 ='https://books.toscrape.com/catalogue/category/books/childrens_11/index.html'		
religion_12 ='https://books.toscrape.com/catalogue/category/books/religion_12/index.html'		
nonfiction_13 ='https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'		
music_14 ='https://books.toscrape.com/catalogue/category/books/music_14/index.html'		
default_15 ='https://books.toscrape.com/catalogue/category/books/default_15/index.html'		
science_fiction_16 ='https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'		
sports_and_games_17 ='https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html'		
add_a_comment_18 ='https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html'		
fantasy_19 ='https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'		
new_adult_20 ='https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html'		
young_adult_21 ='https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html'		
science_22 ='https://books.toscrape.com/catalogue/category/books/science_22/index.html'		
poetry_23 ='https://books.toscrape.com/catalogue/category/books/poetry_23/index.html'		
paranormal_24 ='https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html'		
art_25 ='https://books.toscrape.com/catalogue/category/books/art_25/index.html'		
psychology_26 ='https://books.toscrape.com/catalogue/category/books/psychology_26/index.html'		
autobiography_27 ='https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html'		
parenting_28 ='https://books.toscrape.com/catalogue/category/books/parenting_28/index.html'		
adult_fiction_29 ='https://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html'		
humor_30 ='https://books.toscrape.com/catalogue/category/books/humor_30/index.html'		
horror_31 ='https://books.toscrape.com/catalogue/category/books/horror_31/index.html'		
history_32 ='https://books.toscrape.com/catalogue/category/books/history_32/index.html'		
food_and_drink_33 ='https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html'		
christian_fiction_34 ='https://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html'		
business_35 ='https://books.toscrape.com/catalogue/category/books/business_35/index.html'		
biography_36 ='https://books.toscrape.com/catalogue/category/books/biography_36/index.html'		
thriller_37 ='https://books.toscrape.com/catalogue/category/books/thriller_37/index.html'		
contemporary_38 ='https://books.toscrape.com/catalogue/category/books/contemporary_38/index.html'		
spirituality_39 ='https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html'		
academic_40 ='https://books.toscrape.com/catalogue/category/books/academic_40/index.html'		
self_help_41 ='https://books.toscrape.com/catalogue/category/books/self-help_41/index.html'		
historical_42 ='https://books.toscrape.com/catalogue/category/books/historical_42/index.html'		
christian_43 ='https://books.toscrape.com/catalogue/category/books/christian_43/index.html'		
suspense_44 ='https://books.toscrape.com/catalogue/category/books/suspense_44/index.html'		
short_stories_45 ='https://books.toscrape.com/catalogue/category/books/short-stories_45/index.html'		
novels_46 ='https://books.toscrape.com/catalogue/category/books/novels_46/index.html'		
health_47 ='https://books.toscrape.com/catalogue/category/books/health_47/index.html'		
politics_48 ='https://books.toscrape.com/catalogue/category/books/politics_48/index.html'		
cultural_49 ='https://books.toscrape.com/catalogue/category/books/cultural_49/index.html'		
erotica_50 ='https://books.toscrape.com/catalogue/category/books/erotica_50/index.html'		
crime_51 ='https://books.toscrape.com/catalogue/category/books/crime_51/index.html'		
        

dico_categorie = {
'Books' : books_1,
'Travel' : travel_2,
'Mystery' : mystery_3,
'Historical Fiction' : historical_fiction_4,
'Sequential Art' : sequential_art_5,
'Classics' : classics_6,
'Philosophy' : philosophy_7,
'Romance' : romance_8,
'Womens Fiction' : womens_fiction_9,
'Fiction' : fiction_10,
'Childrens' : childrens_11,
'Religion' : religion_12,
'Nonfiction' : nonfiction_13,
'Music' : music_14,
'Default' : default_15,
'Science Fiction' : science_fiction_16,
'Sports and Games' : sports_and_games_17,
'Add a comment' : add_a_comment_18,
'Fantasy' : fantasy_19,
'New Adult' : new_adult_20,
'Young Adult' : young_adult_21,
'Science' : science_22,
'Poetry' : poetry_23,
'Paranormal' : paranormal_24,
'Art' : art_25,
'Psychology' : psychology_26,
'Autobiography' : autobiography_27,
'Parenting' : parenting_28,
'Adult Fiction' : adult_fiction_29,
'Humor' : humor_30,
'Horror' : horror_31,
'History' : history_32,
'Food and Drink' : food_and_drink_33,
'Christian Fiction' : christian_fiction_34,
'Business' : business_35,
'Biography' : biography_36,
'Thriller' : thriller_37,
'Contemporary' : contemporary_38,
'Spirituality' : spirituality_39,
'Academic' : academic_40,
'Self Help' : self_help_41,
'Historical' : historical_42,
'Christian' : christian_43,
'Suspense' : suspense_44,
'Short Stories' : short_stories_45,
'Novels' : novels_46,
'Health' : health_47,
'Politics' : politics_48,
'Cultural' : cultural_49,
'Erotica' : erotica_50,
'Crime' : crime_51,
}
url_book = []
items_book = []
ask_category = (input(f'What category you want ?{dico_categorie.keys}'))
if ask_category in dico_categorie:
    url_book = module.list_url_book_by_page(dico_categorie[ask_category])
    for url in url_book:
        items_book.append(module.list_item_by_book(url))
    print(len(items_book))