from request import request
from bs4 import BeautifulSoup
import csv
from scrape_book import scrape_book
from scrape_category import scrape_category
from write_file import save_book
from tqdm import tqdm


BASE_DIR = "http://books.toscrape.com/"

def scrape_all_book_category(url_scrape):
    category_list = scrape_category(url_scrape)
    for link in category_list:
        dictionnary_book = scrape_book(link)
        save_book(dictionnary_book)


def scrape(url):
    html = request(url)
    soup = BeautifulSoup(html, "html.parser")
    all_category_list = []
    lis = soup.find("ul", {"class": "nav nav-list"}).find("ul").findAll("li")
    for li in lis:
        link = BASE_DIR + li.find("a")["href"]
        all_category_list.append(link)
    for link in tqdm(all_category_list):
        scrape_all_book_category(link)


scrape(BASE_DIR)


"""
with open('html.txt', 'w') as file:
	file.write(str(soup))
"""


"""

enregistrer le livre en utilisant le module csv


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
"""
--------------------------------------------
- Créer le fichier csv pour une catégorie et la placer dans le bon dossier comme convenu lors de la session
- Télécharger l'ensemble des images d'une catégorie et la placer dans le bon dossier comme convenu lors de la session
- Créer un fichier qui appelle l'ensemble des fonctions pour scrapper une catégorie avec une URL de catégorie en dur
"""
