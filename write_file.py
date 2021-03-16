from pathlib import Path
import csv
from path import pathdir


def save_image(url_image, upc):
	with open(f'{upc}.jpg', "b") as file:
	    file.write(request(url_image))

def write_csv(dictionnary_book):
	category = dictionnary_book['category']
	print(category)
	path = Path(f'/data/{category}/')
	print(path)
	path.mkdir(parents=True, exist_ok=True)
	"""
	filepath = path/f'{category}.csv'
	with filepath.open("a+", newline="", encoding="utf-8") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=dictionnary_book.keys(), delimiter=";")
		if filepath.stat().st_size == 0:
			writer.writeheader()
		writer.writerow(dictionnary_book)
	"""


"""
if Path(filepath).exists():
	with open(filepath, 'a', newline='', encoding='utf-8') as f:
		csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
		csv_writer.writerow(dictionnary_book)
		print('if')
else:
	with open(filepath, 'a', newline='', encoding='utf-8') as f:
		csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
		csv_writer.writeheader()
		csv_writer.writerow(dictionnary_book)
		print('else')
"""



#pathdir(f'/data/{category}/')
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