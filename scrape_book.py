from bs4 import BeautifulSoup
from request import request

BASE_DIR = "http://books.toscrape.com/"


def book_description(description):
    if description:
        description = description.text
    else:
        description = ""
    return description


def book_information(trs):
    sub_book = {}
    for tr in trs:
        th = tr.find("th").text
        td = tr.find("td").text
        sub_book[th] = td
    return sub_book


def scrape_book(url):
    book = {}
    soup = BeautifulSoup(request(url), "html.parser")
    information = book_information(soup.findAll("tr"))
    book["product_page_url"] = url
    book["upc"] = information["UPC"]
    book["title"] = soup.find("article", "product_page").h1.text
    book["price_including_tax"] = information["Price (incl. tax)"]
    book["price_excluding_tax"] = information["Price (excl. tax)"]
    book["number_available"] = information["Availability"]
    book["product_description"] = book_description(
        soup.find("article").find("p", recursive=False)
    )
    book["category"] = soup.ul.find_all("a")[-1].text
    book["review_rating"] = information["Number of reviews"]
    book["image_url"] = soup.find("img")["src"].replace("../../", BASE_DIR)
    return book
