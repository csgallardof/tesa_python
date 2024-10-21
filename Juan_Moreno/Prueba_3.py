import pandas as pd
import telebot
import logging
import os
import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuración del bot de Telegram
BOT_TOKEN = '7909429550:AAEOm3QvTzdLvZNM6Av2YIeCA4bpG6qg2bc'  # Inserta tu token directamente aquí
bot = telebot.TeleBot(BOT_TOKEN)

# Función para hacer web scraping
def scrape_mercadolibre():
    url = 'https://listado.mercadolibre.com.ec/celulares-y-telefonia/celulares-y-smartphones/xiaomi/celulares_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D2%26applied_value_id%3D59387%26applied_value_name%3DXiaomi%26applied_value_order%3D3%26applied_value_results%3D234%26is_custom%3Dfalse'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        logging.info(f"Código de estado HTTP: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')

        phones = []
        items = soup.find_all('li', class_='ui-search-layout__item')
        logging.info(f"Número de items encontrados: {len(items)}")

        for item in items:
            logging.debug(f"HTML del item: {item}")

            name_elem = item.find('h2', class_='ui-search-item__title')
            price_elem = item.find('span', class_='price-tag-fraction')

            # Buscar el descuento
            discount_elem = item.find('span', class_='andes-money-amount__discount')  # Clase actualizada

            if name_elem and price_elem:
                name = name_elem.text.strip()
                price = price_elem.text.strip()
                discount = discount_elem.text.strip() if discount_elem else "No discount"
                phones.append((name, price, discount))
                logging.debug(f"Teléfono encontrado: {name} - {price} - {discount}")
            else:
                logging.warning("Elemento no encontrado en un item")

        logging.info(f"Total de teléfonos extraídos: {len(phones)}")
        return phones

    except requests.RequestException as e:
        logging.error(f"Error al hacer la solicitud HTTP: {e}")
        return []
    except Exception as e:
        logging.error(f"Error inesperado durante el scraping: {e}")
        return []

# Función para actualizar la base de datos
def update_database(phones):
    try:
        conn = sqlite3.connect('phones.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS phones (name TEXT, price TEXT, discount TEXT)''')
        if phones:
            cursor.executemany('INSERT INTO phones (name, price, discount) VALUES (?, ?, ?)', phones)
        conn.commit()
        conn.close()
        logging.info("Base de datos actualizada correctamente.")
    except sqlite3.Error as e:
        logging.error(f"Error al actualizar la base de datos: {e}")

# Función principal
def main():
    logging.info("Iniciando scraping...")
    phones = scrape_mercadolibre()
    
    logging.info("Actualizando base de datos...")
    update_database(phones)
    logging.info("Base de datos actualizada. Iniciando bot...")
    bot.polling()

if __name__ == "__main__":
    main()
