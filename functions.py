def book_description(description): #retourne la description du livre
	if description:
		description = description.text
	else:
		description = ""
	return description

def book_category(lis): # récupération catégorie
	links_a = [] # liste 
	for li in lis:
		if li.find('a'):
			links_a.append(li.find('a').text)
	return links_a[2]

def book_information(trs): # Création d'un dictionnaire pour récupérer les product information
	sub_book = {}
	for tr in trs: 
		th = tr.find('th').text
		td = tr.find('td').text
		sub_book[th] = td
	return sub_book