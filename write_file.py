def save_image(url_image, upc):
	with open(f'{upc}.jpg', "b") as file:
	    file.write(request(url_image))

def
with open('books.csv', 'a', newline='', encoding='utf-8') as f:
	csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
	csv_writer.writeheader()
	csv_writer.writerow(dictionnary_book)