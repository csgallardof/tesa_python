import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio
import psycopg2

#DAtos para que funciones bot telegram y id de usuario
#TELEGRAM_TOKEN = "8038260275:AAGe2R33fVyo2JvLw_DuhAdJ79THeLdMfsM"
#CHAT_ID = "1271362249"

# Función asincorna que envia mensajes a Telegram
#async def send_message_to_telegram(message):
#    bot = Bot(token=TELEGRAM_TOKEN)
#    await bot.send_message(chat_id=CHAT_ID, text=message)

# Función principal
#async def main():
def main():
    
    # Datos de conexión a Base

    hostname = '155.138.253.162'     # Dirección IP o hostname del servidor remoto
    database = 'tesa_python_db'   # Nombre de la base de datos
    username = 'postgres'        # Nombre de usuario de la base de datos
    password = 'JHEQWR2ZUASDasdgASd98x'        # Contraseña de la base de datos
    port = '5432'                     # Puerto, generalmente 5432 para PostgreSQL

    #parte de web scraping
    
    # URL del examen
    url = 'https://listado.mercadolibre.com.ec/celulares-y-telefonia/celulares-y-smartphones/xiaomi/celulares_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D2%26applied_value_id%3D59387%26applied_value_name%3DXiaomi%26applied_value_order%3D3%26applied_value_results%3D234%26is_custom%3Dfalse'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #datos de telefonos
    lista_telefonos = []

    # Encontrar todos los productos
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

            # nombre y el precio
        lista_telefonos.append((name, price))  

    # Conectar a la base de datos
        try:
            connection = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=password,
            port=port
            )
            cursor = connection.cursor()

            # Inserta datos en la base
            cursor.executemany('''
                INSERT INTO erosas_bot (nombre, precio) VALUES (%s, %s)
            ''', lista_telefonos)
            connection.commit()

            # Cerrar conexión a la base
            cursor.close()
            connection.close()
        except Exception as error:
            print(f"Error al conectar a la base de datos: {error}")

        # Preparar el mensaje para Telegram
    message = "\n".join([f"Nombre: {phone[0]}, Precio: {phone[1]}" for phone in lista_telefonos])

        # Enviar el mensaje a Telegram
        #await send_message_to_telegram(message)

        # Imprimir en consola
    print(message)

    # Ejecutar la función principal
    #asyncio.run(main())


if __name__ == "__main__":
    main()