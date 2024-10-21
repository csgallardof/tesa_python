from  bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get (input ("Ingrese la URL de su producto: "))

soup = BeautifulSoup(url.content,"html.parser")

resultado = soup.find("span", {"class": "andes-money-amount__fraction"})


precioActual = resultado.text
precioActual = float(precioActual)


precio_deseado = float(input("Ingrese el precio deseado: "))
print("El precio actual es:",precioActual)
print("Su precio deseado es:",precio_deseado)

if precio_deseado > precioActual:
    print("Existe una oferta")
else:
    print("No existe ninguna oferta")