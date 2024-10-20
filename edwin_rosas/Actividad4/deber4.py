import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests

url_guardadas = []
precios = []


# cantidad de url a consultar
cantidad = input("Por favor, ingresa la cantidad de URL que vas a consultar: ")
cantidad = int(cantidad)

# URL a consultar, debe ser de Patio Tuerca
for i in range(cantidad):
    url = input(f"Ingrese la URL #{i + 1} a consultar : ")  # Obtener la URL del usuario
    url_guardadas.append(url)  # se almacenara segun la cantidad de URL a consultar

# precios
for url in url_guardadas:
    response = requests.get(url)
    resultado = BeautifulSoup(response.content, "html.parser").find("meta", {"itemprop": "price"}) 
    precio = float(resultado['content']) if resultado else None  
    precios.append(precio)

# Guardar resultados

with open('precios.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Precio'])
    for url, precio in zip(url_guardadas, precios):
        writer.writerow([url, precio if precio is not None else 'No disponible']) # en caso de obtener el precio

# Leer CSV
df = pd.read_csv('precios.csv')

print(df[['URL', 'Precio']])