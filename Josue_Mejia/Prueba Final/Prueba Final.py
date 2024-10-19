import requests
from bs4 import BeautifulSoup
import sqlite3
from telegram import Bot

# Configuración del bot de Telegram
TELEGRAM_TOKEN = "7734917809:AAFI2N5ZEaDDrewQ_pw7b8nP70SDQqc6BQU"
CHAT_ID = '1901626072'

# URL de la página que deseas scrape
url = 'https://listado.mercadolibre.com.ec/celulares-y-telefonia/celulares-y-smartphones/xiaomi/celulares_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D2%26applied_value_id%3D59387%26applied_value_name%3DXiaomi%26applied_value_order%3D3%26applied_value_results%3D234%26is_custom%3Dfalse'

# Hacer la solicitud a la página
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Lista para almacenar los nombres y precios de los teléfonos
phones_data = []

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los elementos de productos
    products = soup.find_all('div', class_='ui-search-result__wrapper')

    for product in products:
        # Obtener el nombre del teléfono desde el enlace
        name_element = product.find('a')  # Seleccionamos el primer <a> que contiene el nombre
        name = name_element.text.strip() if name_element else 'No disponible'

        # Obtener el precio del teléfono
        price_element = product.find('span', class_='andes-money-amount__fraction')
        cents_element = product.find('span', class_='andes-money-amount__cents')

        if price_element:
            price = f"{price_element.text.strip()}."  # Parte entera
            if cents_element:
                price += cents_element.text.strip()  # Parte decimal
            price = f"US$ {price}"  # Formatear el precio con la moneda
        else:
            price = 'No disponible'

        # Agregar el nombre y el precio a la lista
        phones_data.append({'nombre': name, 'precio': price})

# Conectar a la base de datos
conn = sqlite3.connect('phones.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price TEXT
)
''')

# Insertar los datos en la base de datos
for phone in phones_data:
    cursor.execute('''
    INSERT INTO phones (name, price)
    VALUES (?, ?)
    ''', (phone['nombre'], phone['precio']))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

# Imprimir la lista de nombres y precios y enviar mensaje a Telegram
message = ""
for phone in phones_data:
    message += f"Nombre: {phone['nombre']}, Precio: {phone['precio']}\n"

# Función para enviar mensajes a Telegram
def send_message_to_telegram(message):
    bot = Bot(token='7734917809:AAFI2N5ZEaDDrewQ_pw7b8nP70SDQqc6BQU')
    bot.send_message(chat_id = '1901626072', text = message)

# Enviar el mensaje a Telegram
send_message_to_telegram(message)

# Imprimir en consola
print(message)



