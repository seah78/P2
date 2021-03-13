with open("imageTitre.jpg", "b") as file:
    file.write(request(url_image))

with open('books.csv', 'a', newline='', encoding='utf-8') as f:
	csv_writer = csv.DictWriter(f, dictionnary_book.keys(), delimiter=';', dialect='excel') 
	csv_writer.writeheader()
	csv_writer.writerow(dictionnary_book)