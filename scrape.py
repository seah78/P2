import requests
from bs4 import BeautifulSoup
from functions import *

temp_url = 'http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/'

def request(url):
	response = requests.get(url)
	if response.ok:
		return response.content

def scrape_book(url):
	book = {} # dictionnaire, les {} peuvent être remplacé par dict() pour plus de clarté
	soup = BeautifulSoup(request(url), 'html.parser')
	information = book_information(soup.findAll('tr'))
	book['product_page_url'] = url 											#product_page_url
	book['upc'] = information['UPC'] 											#universal_ product_code (upc)
	book['title'] = soup.find('article', 'product_page').h1.text 			#title
	book['price_including_tax'] = information['Price (incl. tax)']   #sub_book['Price (incl. tax)'] 			#price_including_tax
	book['price_excluding_tax'] = information['Price (excl. tax)']				#price_excluding_tax
	book['number_available'] = information['Availability'] 					#number_available
	book['product_description'] = book_description(soup.find('article').find('p', recursive=False)) #description								#product_description
	book['category'] = book_category(soup.find('ul', 'breadcrumb').select('li'))   #links_a[2] 											#category
	book['review_rating'] = information['Number of reviews'] 					#review_rating
	book['image_url'] = url + soup.find('img')['src'].replace('../../', '') #image_url
	return book

dictionnary_book = scrape_book(temp_url)
print(dictionnary_book)