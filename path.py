from pathlib import Path

# Vérification et création du dossier data si inexistant


def pathdir(path):

    if Path(path).exists() == False:
        print("Dossier inexistant")
        path.mkdir(parents=True, exist_ok=True)
    else:
        print("Dossier existant")


# Path.stat() pour vérifier si header existe dans mon csv
