import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
import pandas as pd


try:
    conn = mysql.connector.connect(
        host='localhost',
        database='deberes',
        user='root',
        password=''  # No tiene clave
    )
    if conn.is_connected():
        print('Conexión exitosa a la base de datos MySQL')

        cursor = conn.cursor()

      
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS deberes_general (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            descripcion TEXT,
            estado VARCHAR(50)
        )
        """)
        conn.commit()

      
        def scrape_deberes():
            url = 'http://localhost/phpmyadmin/'  
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP erróneos

            soup = BeautifulSoup(response.content, 'html.parser')

            deberes = []
            items = soup.find_all('TAG_QUE_CONTIENE_CADA_DEBER')  # Reemplaza con el tag correcto

            for item in items:
                titulo = item.find('TAG_DEL_TITULO').text.strip()  # Reemplaza con el tag correcto
                descripcion = item.find('TAG_DE_LA_DESCRIPCION').text.strip() if item.find('TAG_DE_LA_DESCRIPCION') else "Sin descripción"  # Reemplaza con el tag correcto
                estado = item.find('TAG_DEL_ESTADO').text.strip() if item.find('TAG_DEL_ESTADO') else "pendiente"  # Reemplaza con el tag correcto
                deberes.append((titulo, descripcion, estado))

            return deberes

       
        deberes = scrape_deberes()

        cursor.executemany('INSERT INTO deberes_general (titulo, descripcion, estado) VALUES (%s, %s, %s)', deberes)
        conn.commit()
        print('Datos insertados correctamente en la base de datos.')

       
        query = "SELECT * FROM deberes_general;"
        df = pd.read_sql(query, conn)

        
        print(df)

except Error as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    if conn.is_connected():
        conn.close()
        print('Conexión a MySQL cerrada')
