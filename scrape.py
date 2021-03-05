import requests
from bs4 import BeautifulSoup

from scrape_book import scrape_book

temp_url = 'http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/'




dictionnary_book = scrape_book(temp_url)

bookcsv = open('books.csv', 'w')
bookcsv.write('product_page_url' + ';' + 'upc' + ';' + 'title' + ';' + 'price_including_tax' + ';' + 'price_excluding_tax' + ';' + 'number_available' + ';' + 'product_description' + ';' + 'category' + ';' + 'review_rating' + ';' + 'image_url' + '\n')
bookcsv.write(dictionnary_book['product_page_url'] + ';' +  dictionnary_book['upc'] + ';' +  dictionnary_book['title'] + ';' +  dictionnary_book['price_including_tax'] + ';' +  dictionnary_book['price_excluding_tax'] + ';' +  dictionnary_book['number_available'] + ';' +   dictionnary_book['product_description'] + ';' +  dictionnary_book['category'] + ';' +  dictionnary_book['review_rating'] + ';' +  dictionnary_book['image_url'] + '\n')
