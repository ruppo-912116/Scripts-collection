import requests
from lxml import html
from bs4 import BeautifulSoup

url = "https://wetten.overheid.nl/BWBR0045754/2022-05-01/0#Hoofdstuk5"

my_dict = {}


# get the html page
htmlPage = requests.get(url).text

# get a new html dom from string
soup = BeautifulSoup(htmlPage,'html.parser')

# find all the div with class hoofdstuk
lawDivs = soup.find_all("div",class_="hoofdstuk") 

for law in lawDivs:
    articleDiv = law.find("div", {"class": "artikel"})
    articleLawHeaderDiv = articleDiv.div
    print(articleLawHeaderDiv)
    print('-----------------------------------------------------')
    break
# [@id="HoofdstukI"]




