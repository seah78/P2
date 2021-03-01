
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
	book['product_page_url']=url 									#product_page_url
	book['title']=soup.find('article', 'product_page').h1.text 		#title

	trs = soup.findAll('tr')
	#[print(str(tr) + '\n\n') for tr in trs]
	for tr in trs:
		th = tr.find('th').text
		td = tr.find('td').text
		print(th + ' ' + td)


	return book

a = scrape_book(temp_url)
print(a)

"""



#universal_ product_code (upc)

price_including_tax
price_excluding_tax
number_available
	book['product_description']=soup.find('div', {'id': 'product_description'}).p.text #product_description
category
review_rating
image_url
"""




"""
<tr>
<th>UPC</th><td>a22124811bfa8350</td>
</tr>


<tr>
<th>Product Type</th><td>Books</td>
</tr>


<tr>
<th>Price (excl. tax)</th><td>£45.17</td>
</tr>


<tr>
<th>Price (incl. tax)</th><td>£45.17</td>
</tr>


<tr>
<th>Tax</th><td>£0.00</td>
</tr>


<tr>
<th>Availability</th>
<td>In stock (19 available)</td>
</tr>


<tr>
<th>Number of reviews</th>
<td>0</td>
</tr>
"""