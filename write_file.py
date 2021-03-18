from pathlib import Path
import csv
from request import request


def save_book(dictionnary_book):
    upc = dictionnary_book["upc"]
    url_image = dictionnary_book["image_url"]
    category = dictionnary_book["category"]
    path = Path(f"./data/{category}/")
    path_image = Path(f"./data/{category}/image/")
    path_image.mkdir(parents=True, exist_ok=True)
    filepath = path / f"{category}.csv"
    filepath_image = path_image / f"{upc}.jpg"
    with filepath.open("a+", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=dictionnary_book.keys(), delimiter=";"
        )
        if filepath.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(dictionnary_book)
    with filepath_image.open("wb") as imgfile:
        imgfile.write(request(url_image))
