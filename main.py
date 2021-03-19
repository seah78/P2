import csv
from bs4 import BeautifulSoup
from tqdm import tqdm
from request import request
from scrape_book import scrape_book
from scrape_category import scrape_category
from write_file import save_book

BASE_DIR = "http://books.toscrape.com/"


def scrape_all_book_category(url_scrape):
    category_list = scrape_category(url_scrape)
    for link in category_list:
        dictionnary_book = scrape_book(link)
        save_book(dictionnary_book)


def scrape(url):
    html = request(url)
    soup = BeautifulSoup(html, "html.parser")
    all_category_list = []
    lis = soup.find("ul", {"class": "nav nav-list"}).find("ul").findAll("li")
    for li in lis:
        link = BASE_DIR + li.find("a")["href"]
        all_category_list.append(link)
    for link in tqdm(all_category_list):
        scrape_all_book_category(link)


scrape(BASE_DIR)
