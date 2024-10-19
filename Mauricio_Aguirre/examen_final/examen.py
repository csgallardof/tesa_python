import requests
from bs4 import BeautifulSoup
import mysql.connector
import datetime
import logging

def extraer_y_almacenar_precio(url, precio_deseado):
    """
    Extrae el precio de un producto de una URL dada y lo almacena o actualiza en una base de datos MySQL.

    Args:
        url (str): La URL del producto.
        precio_deseado (float): El precio máximo deseado para el producto.
    """

    logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Realizar la solicitud HTTP y obtener el contenido de la página
        response = requests.get(url)
        response.raise_for_status()

        # Parsear el HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraer los datos relevantes de la página
        precio_element = soup.find("span", class_="andes-money-amount__fraction")
        precio_texto = precio_element.text
        precio_actual = float(precio_texto.replace(',', ''))

        nombre_producto = soup.find("h1", class_="ui-pdp-title")
        if nombre_producto:
            nombre_producto = nombre_producto.text.strip()
        else:
            nombre_producto = "No se encontró el nombre del producto"

        # Conectar a la base de datos MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_examen_python"
        )

        mycursor = mydb.cursor()

        # Verificar si el producto ya existe en la base de datos
        mycursor.execute("SELECT * FROM productos WHERE url=%s", (url,))
        existing_product = mycursor.fetchone()

        if existing_product:
            # Actualizar el registro existente si el precio es diferente
            if existing_product[2] != precio_actual:
                sql = "UPDATE productos SET precio=%s, fecha_extraccion=NOW() WHERE url=%s"
                val = (precio_actual, url)
                mycursor.execute(sql, val)
                print("El precio del producto ha sido actualizado.")
            else:
                print("El producto ya existe en la base de datos y el precio no ha cambiado.")
        else:
            # Insertar un nuevo registro
            sql = "INSERT INTO productos (url, nombre, precio, fecha_extraccion) VALUES (%s, %s, %s, NOW())"
            val = (url, nombre_producto, precio_actual)
            mycursor.execute(sql, val)
            print("El producto se ha agregado a la base de datos.")

        mydb.commit()
        mycursor.close()
        mydb.close()

        if precio_actual <= precio_deseado:
            print(f"El precio actual ({precio_actual}) es menor o igual al precio deseado. ¡Hay una oferta!")
        else:
            print("No se encontro producto con el precio solicitado")
            print("Asi que no hay ofertas par mostrar")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error en la solicitud HTTP: {e}")
        print("Ocurrió un error al obtener la página web.")
    except ValueError as e:
        logging.error(f"Error al convertir el precio: {e}")
        print("El precio no tiene un formato válido.")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        print("Ocurrió un error inesperado.")

# Ejemplo de uso
url = "https://www.mercadolibre.com.ec/infinix-note-40-pro-dual-sim-256-gb-dorado-8-gb-ram/p/MEC35611833?pdp_filters=category%3AMEC1055#polycard_client=search-nordic&searchVariation=MEC35611833&position=2&search_layout=stack&type=product&tracking_id=f046bdc0-c850-4970-9f1a-7df9c7e25dea&wid=MEC57422352&sid=search"
precio_deseado = 520.0
extraer_y_almacenar_precio(url, precio_deseado)