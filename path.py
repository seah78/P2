from pathlib import Path

# Vérification et création du dossier data si inexistant

def pathdir(path):

	if Path(path).exists() == False :
		print('Dossier inexistant')
		Path(path).mkdir(exist_ok=False)
	else:
		print('Dossier existant')

#Path.stat() pour vérifier si header existe dans mon csv

