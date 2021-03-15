from pathlib import Path
import csv
from path import pathdir


def save_image(url_image, upc):
	with open(f'{upc}.jpg', "b") as file:
	    file.write(request(url_image))

def write_csv(dictionnary_book):
	
	category = dictionnary_book['category']
	"""
	path = Path(f'/data/{category}/')
	path.mkdir(parents=True,exist_ok=True)
	#filepath = path/f'{category}.csv'
	if Path(f'/data/{category}/{category}.csv').exists():
		with open(f'/data/{category}/{category}.csv', 'a', newline='', encoding='utf-8') as f:
			csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
			csv_writer.writerow(dictionnary_book)
			print('if')
	else:
		with open(f'/data/{category}/{category}.csv', 'a', newline='', encoding='utf-8') as f:
			csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
			csv_writer.writeheader()
			csv_writer.writerow(dictionnary_book)
			print('else')
	"""



	pathdir(f'/data/{category}/')
	"""
	if Path(f'/data/{category}/{category}.csv').exists():
		with open(f'/data/{category}/{category}.csv', 'a', newline='', encoding='utf-8') as f:
			csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
			csv_writer.writerow(dictionnary_book)
			print('if')
	else:
		with open(f'/data/{category}/{category}.csv', 'a', newline='', encoding='utf-8') as f:
			csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
			csv_writer.writeheader()
			csv_writer.writerow(dictionnary_book)
			print('else')
	"""
"""
data/nom_de_category/nom_de_category.csv
data/nom_de_category/images/upcOutitreImage.jpg


path = Path(".") /data/"Mettre le nom de la catégorie"
path.mkdir(parents=True, exist_ok=True)
filepath = path / "Mettre le nom de la catégorie.csv"
Et ensuite tu fait direct
with filepath.open("w", newline='', encoding='utf-8') as f:
"""