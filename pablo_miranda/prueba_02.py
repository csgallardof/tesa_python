from  bs4 import BeautifulSoup

import json
import time
import requests
import webbrowser

url = requests.get('https://www.fybeca.com/dermocosmetica/proteccion-solar-2/?start=0&sz=18&maxsize=36')
soup = BeautifulSoup(url.content,"html.parser")
resultado = soup.find_all("div",{"class","product-tile"})

data = []
for product in resultado:
         href = product.find('a')['href']
         name = product.find('a',{'class':'link'}).text
         price = product.find('span',{'class':'value'}).text
         data.append({
              "Name":name.strip(),
              "Price":price.strip(),
              "URL": 'https://www.fybeca.com' + href.strip()
         })

json_str = json.dumps(data, indent=2)

print(json_str)