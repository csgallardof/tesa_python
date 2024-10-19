from  bs4 import BeautifulSoup

import json
import time
import requests
import webbrowser
import unicodecsv as csv

url = requests.get('https://listado.mercadolibre.com.ec/iphone#D[A:iphone]')
soup = BeautifulSoup(url.content,"html.parser")
resultado = soup.find_all("div",{"class","poly-card poly-card--list"})

scraped_data = []
for product in resultado:
         href = product.find('a')['href']
         name = product.find('h2',{'class':'poly-box poly-component__title'}).text
         price = product.find('div',{'class':'poly-price__current'}).text
         scraped_data.append({
              "Name":name.strip(),
              "Price":price.strip(),
              "URL": href.strip()
         })

if scraped_data:
    print ("Writing scraped data...")
    with open('scrapped_data_mercado_libre.csv','wb') as csvfile:
        fieldnames = ["Name","Price","URL"]
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for data in scraped_data:
            writer.writerow(data)

    print("Sending message to telegram...")
    
    TOKEN = "bot_token"
    chat_id = "chat_id"
    message = "Listado de iPhones ML"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    #print(requests.get(url).json())
else:
    print("No data scraped")