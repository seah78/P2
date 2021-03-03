import requests
from bs4 import BeautifulSoup

temp_url = 'http://books.toscrape.com/catalogue/sharp-objects_997/'

def request(url):
	response = requests.get(url)
	if response.ok:
		return response.content

#def description
# soup.select('h1') renvoi liste contenant tous les h1
# find
# findAll


def scrape_book(url):
	book = {} # dict()
	sub_book = {}
	soup = BeautifulSoup(request(url), 'html.parser')
	trs = soup.findAll('tr')
	#[print(str(tr) + '\n\n') for tr in trs]
	for tr in trs:
		th = tr.find('th').text
		td = tr.find('td').text
		sub_book[th] = td # ajout des product information à un sous-dictionnaire
		#print(th + ' ' + td)
	links_a = []
	lis = soup.find('ul', 'breadcrumb').findAll('li')
	for li in lis:
		if li.find('a'):
			links_a.append(li.find('a').text)	
			

	#print(str(sub_book) + '\n\n')

	book['product_page_url'] = url 											#product_page_url
	book['upc'] = sub_book['UPC'] 											#universal_ product_code (upc)
	book['title'] = soup.find('article', 'product_page').h1.text 			#title
	book['price_including_tax'] = sub_book['Price (incl. tax)'] 			#price_including_tax
	book['price_excluding_tax'] = sub_book['Price (excl. tax)']				#price_excluding_tax
	book['number_available'] = sub_book['Availability'] 					#number_available
	description = soup.find('article').find('p', recursive=False)
	if description:
		description = description.text
	else:
		description = ""
	book['product_description'] = description								#product_description
	book['category'] = links_a[2] #category
	book['review_rating'] = sub_book['Number of reviews'] 					#review_rating
	book['image_url'] = url + soup.find('img')['src'].replace('../../', '') #image_url

	return book

dictionnary_book = scrape_book(temp_url)
print(dictionnary_book)

