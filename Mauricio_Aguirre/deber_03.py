from  bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://www.mercadolibre.com.ec/infinix-note-40-pro-dual-sim-256-gb-dorado-8-gb-ram/p/MEC35611833?pdp_filters=category%3AMEC1055#polycard_client=search-nordic&searchVariation=MEC35611833&position=2&search_layout=stack&type=product&tracking_id=f046bdc0-c850-4970-9f1a-7df9c7e25dea&wid=MEC574223552&sid=search")

soup = BeautifulSoup(url.content,"html.parser")

resultado = soup.find("span",{"class","andes-money-amount__fraction"})

print(resultado)

precioActual_text = resultado.text
print(precioActual_text)

precioActual = float(precioActual_text)

print(precioActual)

precioDeseado = float(260)

print(precioDeseado)

if precioDeseado > precioActual:
    print("Existe una oferta")
else:
    print("No existe ninguna oferta")
