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
lawDivs = soup.find_all("div",class_="hoofdstuk") 

ulCount = -1
liCount = -1

ulDiv = []
liDiv = []
nestedUlDiv = []

def recursiveChildFinder(ulDiv):
    print("---------------------recursion---------------------------")
    
    if(ulDiv == 'end'):
        return
    
    liDiv = ulDiv.find_all("li")

    for li in liDiv:
        pDiv = li.find('p')
        if(pDiv == None):
            continue
        span = pDiv.find("span").text
        my_dict[mainArticleNumber+span] = pDiv.get_text()
        
        nestedUl = li.find_all('ul')
        if(ulDiv == None):
            continue
        else:
            recursiveChildFinder(next(nestedUl,'end'))
    # recursiveChildFinder(next(ulDiv,'end'))
        
        # for li in liDiv:
        #     nestedUlDiv = li.find('ul')
        #     if(nestedUlDiv != None):
        #         recursiveChildFinder()
            # pDiv = li.find('p')
            # span = pDiv.find("span").get_text()
            # my_dict[mainArticleNumber+span] = pDiv.get_text()
            # recursiveChildFinder(next(nestedUlDiv,"end"))
        # return recursiveChildFinder(next(ulDiv,'end'))
    
    
    
    
    # for ul in ulDiv:
    #     liDiv = ul.find_all("li")
    #     for li in liDiv:
    #         # spanDiv = articleDiv.find("span", {"class": "lidnr"})
    #         pDiv = li.find("p")
    #         if(pDiv == None):
    #             continue
    #         else:
    #             span = pDiv.find("span").get_text()
    #             print(span)
    #             print('-------------------------')
    #             my_dict[mainArticleNumber + span] = pDiv.get_text()
    #         # print(li.find("span"),{ "class" : "lidnr" })
    #         # print('----------------------------------')
    #         recursiveChildFinder(li)

for law in lawDivs:
    articleDiv = law.find("div", {"class": "artikel"})
    mainArticleNumber = articleDiv.get("id")
    articleLawHeaderDiv = articleDiv.div
    
    mainPDiv = articleDiv.find("p",{"class": "al"})
    if(mainPDiv != None):
        my_dict[mainArticleNumber] = mainPDiv.get_text()
     
    ulDiv = iter(articleDiv.find_all("ul"))
    if(ulDiv == None):
        continue
    recursiveChildFinder(next(ulDiv, 'end'))
    mainArticleNumber = ""
            

# write the dictionary to json
with open("article.json", "w") as fp:
    json.dump(my_dict, fp, indent=2)




