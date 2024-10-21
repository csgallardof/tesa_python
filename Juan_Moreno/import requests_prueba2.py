import requests
from bs4 import BeautifulSoup


url = 'https://es.wikipedia.org/wiki/Mormyroidea'


response = requests.get(url)


if response.status_code == 200:
    # Crear el objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

   
    intro_paragraph = soup.find('p').get_text()

   
    print("Información extraída del artículo de Wikipedia sobre Mormyroidea:")
    print(intro_paragraph)

    
    with open('mormyroidea_info.txt', 'w', encoding='utf-8') as file:
        file.write("Información extraída de Wikipedia sobre Mormyroidea:\n\n")
        file.write(intro_paragraph)
else:
    print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")
