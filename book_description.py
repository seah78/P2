def book_description(description): #retourne la description du livre
	if description:
		description = description.text
	else:
		description = ""
	return description