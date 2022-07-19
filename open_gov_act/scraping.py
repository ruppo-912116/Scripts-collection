import requests
from lxml import html
from bs4 import BeautifulSoup

url = "https://wetten.overheid.nl/BWBR0045754/2022-05-01/0#Hoofdstuk5"


# get the html page
htmlPage = requests.get(url).text

# get a new html dom from string
soup = BeautifulSoup(htmlPage,'html.parser')

# find all the div with class hoofdstuk
lawDivs = soup.find_all("div",class_="hoofdstuk") 

for law in lawDivs:
    # nestedSoup = law.find("div", class_="artikle")
    nestedSoup = law.find_all("div", {"class": "artikle"})
    print(law.prettify())
    break

# [@id="HoofdstukI"]




