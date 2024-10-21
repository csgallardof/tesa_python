import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def scrape_ecommerce():
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')


    productos = []
    items = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')

    for item in items:
        nombre = item.find('a', class_='title').text.strip()
        precio = item.find('h4', class_='pull-right price').text.strip()
        descripcion = item.find('p', class_='description').text.strip()
        rating = item.find('p', class_='pull-right').text.strip()
        
        productos.append((nombre, precio, descripcion, rating))

    return productos


productos = scrape_ecommerce()


df = pd.DataFrame(productos, columns=['Nombre', 'Precio', 'Descripción', 'Rating'])


print("Primeras filas del DataFrame:")
print(df.head())


print("\nInformación general:")
print(df.info())


print("\nEstadísticas descriptivas:")
print(df.describe())

df['Precio'] = df['Precio'].replace('[\$,]', '', regex=True).astype(float)


plt.figure(figsize=(10, 6))
sns.histplot(df['Precio'], bins=20, kde=True)
plt.title('Distribución de Precios de Productos')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Rating', palette='viridis')
plt.title('Distribución de Ratings de Productos')
plt.xlabel('Cantidad de Productos')
plt.ylabel('Rating')
plt.show()
