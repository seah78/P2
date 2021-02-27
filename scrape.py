
import requests
from bs4 import BeautifulSoup

temp_url = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'

def request(url):
	response = requests.get(url)
	if response.ok:
		return response.content

#def description
# soup.select('h1') renvoi liste contenant tous les h1
# find
# findAll

def scrape_book(url):
	book = dict()
	soup = BeautifulSoup(request(url), 'html.parser')
	book['product_page_url']=url
	book['title']=soup.find('article', 'product_page').h1.text
	return book

a = scrape_book(temp_url)
print(a)

#product_page_url
#universal_ product_code (upc)
#title
#price_including_tax
#price_excluding_tax
#number_available
#product_description
#category
#review_rating
#image_url