import requests
from bs4 import BeautifulSoup
import mysql.connector
from telegram import Bot
import asyncio

# Configuración del bot de Telegram
TELEGRAM_TOKEN = "7995146553:AAFxEEfBeXv21Rl5e_KmIaUFU4LnR9Z2nJQ"
CHAT_ID = '1563347266'

# Función para enviar mensajes a Telegram
async def send_message_to_telegram(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Función principal
async def main():
    # Enviar un mensaje de prueba a Telegram
    await send_message_to_telegram("Mensaje de prueba desde Python")

    # Datos de conexión a MySQL (phpMyAdmin)
    db_config = {
        'user': 'root',        # Cambia esto si es necesario
        'password': '',        # Añade tu contraseña aquí
        'host': 'localhost',   # Cambia esto si es necesario
        'database': 'examen_python',  # Asegúrate de que este nombre sea correcto
    }

    # URL de la página que deseas scrape
    url = 'https://listado.mercadolibre.com.ec/celulares-y-telefonia/celulares-y-smartphones/xiaomi/celulares_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D2%26applied_value_id%3D59387%26applied_value_name%3DXiaomi%26applied_value_order%3D3%26applied_value_results%3D234%26is_custom%3Dfalse'

    # Hacer la solicitud a la página
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # Lista para almacenar los nombres y precios de los teléfonos
    examen_python = []

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el contenido de la página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar todos los elementos de productos
        products = soup.find_all('div', class_='ui-search-result__wrapper')
        for product in products:
            # Obtener el nombre del teléfono desde el enlace
            name_element = product.find('a')
            name = name_element.text.strip() if name_element else 'No disponible'

            # Obtener el precio del teléfono
            price_element = product.find('span', class_='andes-money-amount__fraction')
            cents_element = product.find('span', class_='andes-money-amount__cents')

            if price_element:
                price = f"{price_element.text.strip()}."
                if cents_element:
                    price += cents_element.text.strip()
                price = f"US$ {price}"
            else:
                price = 'No disponible'

            # Agregar el nombre y el precio a la lista
            examen_python.append((name, price))  # Cambiar a tupla

    # Conectar a la base de datos MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Crear una tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS phones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                price VARCHAR(50)
            )
        ''')

        # Insertar los datos en la base de datos
        cursor.executemany('''
            INSERT INTO phones (name, price) VALUES (%s, %s)
        ''', examen_python)
        conn.commit()

        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # Preparar el mensaje para Telegram
    message = "\n".join([f"Nombre: {phone[0]}, Precio: {phone[1]}" for phone in examen_python])

    # Enviar el mensaje a Telegram
    await send_message_to_telegram(message)

    # Imprimir en consola
    print(message)

# Ejecutar la función principal
asyncio.run(main())