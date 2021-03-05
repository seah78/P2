def book_information(trs): # Création d'un dictionnaire pour récupérer les product information
	sub_book = {}
	for tr in trs: 
		th = tr.find('th').text
		td = tr.find('td').text
		sub_book[th] = td
	return sub_book