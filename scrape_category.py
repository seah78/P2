from request import request
from bs4 import BeautifulSoup
import csv
from scrape_book import scrape_book
from pathlib import Path

BASE_DIR = 'http://books.toscrape.com/'
BASE_CAT = 'http://books.toscrape.com/catalogue/category/books'

temp_url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html'
#temp_url = temp_url.replace('index.html', '') #prévoir une condition si index.html n'est pas dans l'url



html = request(temp_url)
soup = BeautifulSoup(html, 'html.parser')

def category_list(soup):
	lis = soup.find('ul', 'nav nav-list').find('ul').findAll('li')
	url_cat_list=[]
	for li in lis:
		link_category = li.find('a')['href'].replace('..', BASE_CAT)
		url_cat_list.append(link_category)
	return url_cat_list

def book_list(soup_cat):
	h3s = soup.findAll('h3') # books url dans balise h3
	url_book_list=[] # création d'une liste
	for h3 in h3s: # boucle qui imprime la liste des urls des livres d'une page
		link = h3.find('a')['href'].replace('../../..', BASE_DIR + 'catalogue')
		url_book_list.append(link)
	return url_book_list

for url_cat in category_list(soup):
	html_cat = request(url_cat)
	soup_cat = BeautifulSoup(html_cat, 'html.parser')
	for url_book in book_list(soup_cat):
		print(url_book)

