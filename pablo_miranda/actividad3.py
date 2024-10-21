
from  bs4 import BeautifulSoup

import requests
import time
import webbrowser

url = requests.get('https://www.fybeca.com/protector-solar-sun-fresh-derm-care-sin-color-fps-70-40-g-1-unidad/ECFY_527574.html')
soup = BeautifulSoup(url.content,"html.parser")
nombre = soup.find("a",{"class","product-brand"})
#print(nombre)

nombre_actual_text = nombre.text
print(nombre_actual_text)

precio = soup.find("div",{"class","large-price"})
print(precio)

precio_actual_text = precio.text
print(precio_actual_text)