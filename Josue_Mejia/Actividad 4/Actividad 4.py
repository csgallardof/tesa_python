from  bs4 import BeautifulSoup
import requests
import time
import webbrowser
import csv
import pandas as pd

url_guardadas = []
precios = []

for i in range(5):
    url = input(f"Ingrese la URL del producto {i + 1}: ")  # Obtener la URL del usuario
    url_guardadas.append(url)  # Agregar la URL a la lista

# Extraer precios
for url in url_guardadas:
    response = requests.get(url)
    resultado = BeautifulSoup(response.content, "html.parser").find("span", {"class": "andes-money-amount__fraction"})
    precioActual = float(resultado.text.replace('.', '').replace(',', '.').strip()) if resultado else None
    precios.append(precioActual)

# Guardar resultados en un archivo CSV
with open('precios_productos.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Precio'])
    for url, precio in zip(url_guardadas, precios):
        writer.writerow([url, precio if precio is not None else 'No disponible'])

# Leer el archivo CSV
df = pd.read_csv('precios_productos.csv')

# Convertir la columna 'Precio' a tipo numérico (manejar errores para valores no convertibles)
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')

# Ordenar el DataFrame por precios de forma descendente
df_sorted = df.sort_values(by='Precio', ascending=False)

# Imprimir el DataFrame ordenado
print(df_sorted[['URL', 'Precio']])