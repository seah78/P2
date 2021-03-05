def book_category(lis): # récupération catégorie
	links_a = [] # liste 
	for li in lis:
		if li.find('a'):
			links_a.append(li.find('a').text)
	return links_a[2]