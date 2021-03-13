from bs4 import BeautifulSoup
from request import request

BASE_DIR = 'http://books.toscrape.com/'

def book_description(description): #retourne la description du livre
	if description:
		description = description.text
	else:
		description = ""
	return description

def book_information(trs): # Création d'un dictionnaire pour récupérer les product information
	sub_book = {}
	for tr in trs: 
		th = tr.find('th').text
		td = tr.find('td').text
		sub_book[th] = td
	return sub_book

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
	book['category'] = soup.ul.find_all("a")[-1].text	#category
	book['review_rating'] = information['Number of reviews'] 					#review_rating
	book['image_url'] =  soup.find('img')['src'].replace('../../', BASE_DIR) #image_url
	return book