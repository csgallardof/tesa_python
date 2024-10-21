import requests
from bs4 import BeautifulSoup

# URL de la página de Wikipedia
url = 'https://es.wikipedia.org/wiki/Mormyroidea'

# Realizar la solicitud HTTP a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Crear el objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer el primer párrafo del artículo
    intro_paragraph = soup.find('p').get_text()

    # Mostrar el párrafo extraído
    print("Información extraída del artículo de Wikipedia sobre Mormyroidea:")
    print(intro_paragraph)

    # Guardar la información en un archivo
    with open('mormyroidea_info.txt', 'w', encoding='utf-8') as file:
        file.write("Información extraída de Wikipedia sobre Mormyroidea:\n\n")
        file.write(intro_paragraph)
else:
    print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")
