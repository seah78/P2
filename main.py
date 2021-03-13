from request import request
from bs4 import BeautifulSoup
import csv
from scrape_book import scrape_book
from path import pathdir

pathdir('data')


"""
page_next = soup.find('ul', 'pager').find('li', 'next')
if page_next:
	page = soup.find('ul', 'pager').find('li', 'next').find('a')['href']
	page = BASE_DIR + 'catalogue/category/books/' + category + page
	print(page)
"""

"""
def page_list(url_page):
	html_page = request(url_page)
	soup_page = BeautifulSoup(html, 'html.parser')
	next_page = soup_page.find('ul', 'pager').find('li', 'next')
	print(url_page)
	for next_page:
		page = soup.find('ul', 'pager').find('li', 'next').find('a')['href']
		url_page = url_page.replace('')
		print(page)

"""

#page_list
"""
page_list=[]
page_list.append(temp_url)
p=1
while soup.find('ul', 'pager').find('li', 'next'):
	temp_url = temp_url.replace('index.html', 'page' + str(p) + 'html')
	page_list.append(temp_url)
	html = request(temp_url)
	soup = BeautifulSoup(html, 'html.parser')
	p+=1



print(page_list)
"""



"""
si condition ok alors
	récup livre
	boucle
	"""



"""
dictionnary_book = scrape_book(temp_url)

#Ajout au fichier csv
with open('books.csv', 'w', newline='', encoding='utf-8') as f:
	csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
	csv_writer.writeheader()
	csv_writer.writerow(dictionnary_book)
"""	



"""
récupération des livres d'une catégorie

enregistrer le livre en utilisant le module csv

recherche le next
passage automatique à la page suivante (boucle + condition)

Récupération des links pour chaque livre d'une page
boucle pour scraper un livre
écrire infos dans même fichier csv

gérer les dossiers
data/nom_de_category/nom_de_category.csv
data/nom_de_category/images/upcOutitreImage.jpg

télécharger les images

- Essayer le module csv avec seul fichier
- Faire une fonction qui permet de récupérer l'ensemble des liens de livres d'une catégorie

Bonus : Ecrire tous les livres dans un seul et même fichier csv qui aura pour nom le nom de la catégorie.
-----------------------
Module pathlib : module pour gérer les repertoire

"""

