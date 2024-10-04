
from  bs4 import BeautifulSoup

import requests
import time
import webbrowser

url = requests.get('https://www.fybeca.com/dermocosmetica/proteccion-solar-2/')
soup = BeautifulSoup(url.content,"html.parser")
resultado = soup.find("div",{"class","product-tile"})
print(resultado)

precio_actual_text = resultado.text
print(precio_actual_text)






