import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Hacer una solicitud a la página web
url = "https://www.mercadolibre.com.ec/infinix-note-40-pro-dual-sim-256-gb-dorado-8-gb-ram/p/MEC35611833?pdp_filters=category%3AMEC1055#polycard_client=search-nordic&searchVariation=MEC35611833&position=2&search_layout=stack&type=product&tracking_id=f046bdc0-c850-4970-9f1a-7df9c7e25dea&wid=MEC574223552&sid=search"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer datos (ejemplo: precios de productos)
precios = []
for precio in soup.find_all('span', class_='precio'):
    precios.append(float(precio.text.replace('$', '')))

# Crear un DataFrame de pandas
df = pd.DataFrame({'Precio': precios})

# Crear un histograma
plt.hist(df['Precio'], bins=20)
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Distribución de Precios')
plt.show()