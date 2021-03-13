from request import request
from bs4 import BeautifulSoup
import csv
from scrape_book import scrape_book
from path import pathdir

pathdir('data')






"""
si condition ok alors
	récup livre
	boucle
	"""




dictionnary_book = scrape_book(temp_url)

#Ajout au fichier csv


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
