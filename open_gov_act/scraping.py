import requests
from lxml import html
from bs4 import BeautifulSoup

import json

url = "https://wetten.overheid.nl/BWBR0045754/2022-05-01/0#Hoofdstuk5"

my_dict = {}


# get the html page
htmlPage = requests.get(url).text

# get a new html dom from string
soup = BeautifulSoup(htmlPage,'html.parser')

# find all the div with class hoofdstuk
# pDivs = soup.find_all("p",class_="lid labeled")

articleDiv = soup.find_all("div",class_="artikel")

for article in articleDiv:
    mainContainer = article.findParent()
    idName = mainContainer.get("id")
    pDivs = article.find_all("p",class_="lid labeled")
    
    for pDiv in pDivs:
        print(pDiv.prettify())
        print('--------------------')
        lid_labeled_tracker = pDiv.find('span').text
        labeledDiv = pDiv.findParent().find_all('p',class_="labeled")
        
        subArticleValue = pDiv.find('span').text
        my_dict[idName+"."+subArticleValue] = pDiv.text
            
        # for p in pDivs:
    #     subArticleValue = p.find('span').text
    #     my_dict[idName+"."+subArticleValue] = p.text
        
        for label in labeledDiv:
            subArticleValue1 = label.find('span').text
            label1 = str(idName+'.'+subArticleValue+'.'+subArticleValue1).replace(" ","")
            my_dict[label1] = label.text


print(my_dict)    

# write the dictionary to json
with open("article.json", "w") as fp:
    json.dump(my_dict, fp, indent=2)




