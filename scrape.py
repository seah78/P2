
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

reponse = requests.get(url)

print(reponse)