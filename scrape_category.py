from request import request
from bs4 import BeautifulSoup
import csv
from scrape_book import scrape_book

BASE_DIR = 'http://books.toscrape.com/'
BASE_CAT = 'http://books.toscrape.com/catalogue/category/books'

temp_url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
#temp_url = temp_url.replace('index.html', '') #prévoir une condition si index.html n'est pas dans l'url



def book_list(soup):
	h3s = soup.findAll('h3') # books url dans balise h3
	url_book_list=[] # création d'une liste
	for h3 in h3s: # boucle qui imprime la liste des urls des livres d'une page
		link = h3.find('a')['href'].replace('../../..', BASE_DIR + 'catalogue')
		url_book_list.append(link)
	return url_book_list



def scrape_category(url):
	url_base = url
	html = request(url_base)
	soup = BeautifulSoup(html, 'html.parser')
	all_book_list=[]
	all_book_list.extend(book_list(soup))
	page_next = soup.find('ul', 'pager').find('li', 'next')
	page_number=1
	while page_next:
		page_number += 1
		page_url = url_base.replace('index.html', f'page-{page_number}.html')
		html = request(page_url)
		soup = BeautifulSoup(html, 'html.parser')
		all_book_list.extend(book_list(soup))
		page_next = soup.find('ul', 'pager').find('li', 'next')
	return all_book_list

"""	
fonction qui permet de boucler sur les liens de la catégory et scraper les livres
ajouter au fur et à mesure dans le fichier csv

scrape_category(temp_url)
"""


"""
category = 'sequential-art_5/'
page_next = soup.find('ul', 'pager').find('li', 'next')
if page_next:
	page = soup.find('ul', 'pager').find('li', 'next').find('a')['href']
	page = BASE_DIR + 'catalogue/category/books/' + category + page
	print(page)
"""

"""
while page_next == True:

	condition de sortie : page_next = false
	refaire une soup dans la boucle pour la nouvelle page



"""

"""
for url_cat in category_list(soup):
	html_cat = request(url_cat)
	soup_cat = BeautifulSoup(html_cat, 'html.parser')
	for url_book in book_list(soup_cat):
		print(url_book)
"""
