import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def scrape_web():
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  

    soup = BeautifulSoup(response.content, 'html.parser')


    descripcion = soup.find_all('p')[1].text.strip()


    tabla_clasificacion = soup.find('table', {'class': 'infobox biota'})
    
    clasificacion = {}
    if tabla_clasificacion:
        for fila in tabla_clasificacion.find_all('tr'):
            columnas = fila.find_all('th', 'td')
            if len(columnas) == 2:
                clasificacion[columnas[0].text.strip()] = columnas[1].text.strip()

    return descripcion, clasificacion


descripcion, clasificacion = scrape_web()


print(f"Descripción: {descripcion}")


df_clasificacion = pd.DataFrame(list(clasificacion.items()), columns=['Categoría', 'Valor'])


print(df_clasificacion)


df_clasificacion.to_csv('clasificacion_goura.csv', index=False)


plt.figure(figsize=(10, 6))
sns.barplot(data=df_clasificacion, x='Categoría', y='Valor', palette='viridis')
plt.title('Clasificación Científica de Goura scheepmakeri')
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.show()
