import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página principal de libros
url = "http://books.toscrape.com/catalogue/page-1.html"

# Lista para almacenar los datos
lista_libros = []

# Recorremos
for page in range(1, 6): 
    page_url = f"http://books.toscrape.com/catalogue/page-{page}.html"# Actualizamos la URL de la página actual
    response = requests.get(page_url)

    if response.status_code == 200:
        # Creamos el objeto BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Buscamos todos los libros en la página
        libros = soup.find_all("article", class_="product_pod")

        for libro in libros:
            # Extraemos el título
            title = libro.h3.a["title"]

            # Extraemos el precio
            price = libro.find("p", class_="price_color").text

            # Extraemos la disponibilidad
            availability = libro.find("p", class_="instock availability").text.strip()

            # Guardamos los datos en la lista
            lista_libros.append({
                "Titulo": title,
                "Precio": price,
                "Disponibilidad": availability
            })
    else:
        print(f"Error al cargar la página: {page_url}")

# Convertimos los datos a un DataFrame de pandas
df = pd.DataFrame(lista_libros)

# Guardamos los datos en un archivo CSV
df.to_csv("libros.csv", index=False)

print("Datos guardados en libros.csv")
