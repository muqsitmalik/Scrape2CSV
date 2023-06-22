from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys


def getHtmlContent(product):
    url = f"https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    response = requests.get(url)

    if response.status_code == 200:
        page = BeautifulSoup(response.text,"html.parser")
        return page
    else:
        print("Request failed with status code:", response.status_code)


def saveData(name,price,link):
    data = {'Title' : [] , 'Price' : [] , 'Link' : [] }

    for name in name:
        data['Title'].append(name.string)

    for price in price:
        data['Price'].append(price.string.replace("₹", ""))

    for link in link:
        data["Link"].append("https://www.flipkart.com" + link['href'] + "\n")

    df = pd.DataFrame.from_dict(data)
    df.to_csv("data.csv",index=False)


product = input("Entre product to search: \n")
page = getHtmlContent(product)


name = page.find_all(class_="_4rR01T")
price = page.find_all(class_="_30jeq3 _1_WHN1")
link = page.find_all(class_="_1fQZEK")

if len(name) == 0 or len(price) == 0 or len(link) == 0 :
    print("Product not found.")
    sys.exit()

saveData(name,price,link)






