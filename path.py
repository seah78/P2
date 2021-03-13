from pathlib import Path

# Vérification et création du dossier data si inexistant

def pathdir(path):
	if Path(path).exists() == False :
		Path(path).mkdir(exist_ok=False)
	else:
		print('Le dossier existe déjà')


#Path.stat() pour vérifier si header existe