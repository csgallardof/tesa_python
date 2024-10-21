from  bs4 import BeautifulSoup

import json
import time
import requests
import webbrowser
import unicodecsv as csv

url = requests.get('https://www.fybeca.com/dermocosmetica/proteccion-solar-2/?start=0&sz=6&maxsize=10')
soup = BeautifulSoup(url.content,"html.parser")
resultado = soup.find_all("div",{"class","product-tile"})

scraped_data = []
for product in resultado:
         href = product.find('a')['href']
         name = product.find('a',{'class':'link'}).text
         price = product.find('span',{'class':'value'}).text
         scraped_data.append({
              "Name":name.strip(),
              "Price":price.strip(),
              "URL": 'https://www.fybeca.com' + href.strip()
         })

if scraped_data:
    print ("Writing scraped data to scrapped_data.csv")
    with open('scrapped_data.csv','wb') as csvfile:
        fieldnames = ["Name","Price","URL"]
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for data in scraped_data:
            writer.writerow(data)
else:
    print("No data scraped")