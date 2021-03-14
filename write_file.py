def save_image(url_image, upc):
	with open(f'{upc}.jpg', "b") as file:
	    file.write(request(url_image))

<<<<<<< HEAD
def
with open('books.csv', 'a', newline='', encoding='utf-8') as f:
	csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
	csv_writer.writeheader()
	csv_writer.writerow(dictionnary_book)
=======
def write_csv(dictionnary_book):
	category = dictionnary_book['category']
	with open(f'{category}.csv', 'a', newline='', encoding='utf-8') as f:
		if Path(f'{category}.csv').exists():
			csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
			csv_writer.writerow(dictionnary_book)
		else:
			csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
			csv_writer.writeheader()
			csv_writer.writerow(dictionnary_book)
>>>>>>> fd33b86c507ab77c53057f59a65bcdd6f1fd552e
