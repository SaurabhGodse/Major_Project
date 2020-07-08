import requests
from bs4 import BeautifulSoup

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_electromagnetism_equations"

req = requests.get(WIKI_URL)
soup = BeautifulSoup(req.content, 'lxml')
table_classes = {"class": ["sortable", "plainrowheaders", "wikitable"]}
wikitables = soup.findAll("table", table_classes)

print(wikitables)