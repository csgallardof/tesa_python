from bs4 import BeautifulSoup
import requests

# Solicitar la URL del producto
url = input("Ingrese la URL de su producto: ")

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar el precio utilizando el itemprop
    resultado = soup.find("div", {"itemprop": "offers"})

    if resultado:
        # Extraer el valor del precio del atributo content de la etiqueta <meta>
        precioActual = resultado.find("meta", {"itemprop": "price"})['content']
        precioActual = float(precioActual)  # Convertir el precio a float

        precio_deseado = float(input("Ingrese el precio deseado: "))
        print("El precio actual es:", precioActual)
        print("Su precio deseado es:", precio_deseado)

        if precio_deseado > precioActual:
            print("Existe una oferta")
        else:
            print("No existe ninguna oferta")
    else:
        print("No se pudo encontrar el precio en la página.")
else:
    print(f"Error al acceder a la página: {response.status_code}")