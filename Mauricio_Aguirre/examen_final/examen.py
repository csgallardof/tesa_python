import requests
from bs4 import BeautifulSoup
import mysql.connector
import datetime

def extraer_y_almacenar_precio(url, precio_deseado):
    """
    Extrae el precio de un producto de una URL dada y lo almacena en una base de datos MySQL.

    Args:
        url (str): La URL del producto.
        precio_deseado (float): El precio máximo deseado para el producto.
    """

    try:
        # Realizar la solicitud HTTP y obtener el contenido de la página
        response = requests.get(url)
        response.raise_for_status()

        # Parsear el HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraer los datos relevantes de la página (ajusta los selectores según la estructura de la página)
        precio_element = soup.find("span", class_="andes-money-amount__fraction")
        precio_texto = precio_element.text
        precio_actual = float(precio_texto.replace(',', ''))
        nombre_producto = soup.find("h1", class_="ui-pdp-title").text.strip()

        # Conectar a la base de datos MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_examen_python"
        )

        mycursor = mydb.cursor()

        # Crear la tabla si no existe
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url VARCHAR(255),
                nombre VARCHAR(255),
                precio FLOAT,
                fecha_extraccion DATETIME
            )
        """)

        # Insertar los datos en la tabla
        sql = "INSERT INTO productos (url, nombre, precio, fecha_extraccion) VALUES (%s, %s, %s, NOW())"
        val = (url, nombre_producto, precio_actual)
        mycursor.execute(sql, val)

        mydb.commit()
        mycursor.close()
        mydb.close()

        if precio_actual <= precio_deseado:
            print(f"El precio actual ({precio_actual}) es menor o igual al precio deseado. ¡Hay una oferta!")

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
    except mysql.connector.Error as e:
        print(f"Error en la base de datos: {e}")

# Ejemplo de uso
url = "https://www.mercadolibre.com.ec/infinix-note-40-pro-dual-sim-256-gb-dorado-8-gb-ram/p/MEC35611833?pdp_filters=category%3AMEC1055#polycard_client=search-nordic&searchVariation=MEC35611833&position=2&search_layout=stack&type=product&tracking_id=f046bdc0-c850-4970-9f1a-7df9c7e25dea&wid=MEC574223552&sid=search"
precio_deseado = 329.0
extraer_y_almacenar_precio(url, precio_deseado)