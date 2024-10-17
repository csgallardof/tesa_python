## Ejercicio en clase 

informacion_personal = {"nombre":"Juan",
                        "telefono":"0985413259",
                        "email":"jansebastian11@hotmail.com"
} 

# Contador de palabras dentro de un diccionario


def contar_palabras(informacion_personal):
    
    numero_de_palabras = 0
    
    for valor in informacion_personal.values():
        numero_de_palabras += len(valor.split())
    return numero_de_palabras

resultado = contar_palabras(informacion_personal)

print(f"Total de palabras en el diccionario: {resultado}")



# Mapeo de usuarios

usuarios = ["usuario 1","usuario 2","usuario 3","usuario 4"]

mapeo_usuarios = {i+1:usuario for i, usuario in enumerate(usuarios)}

for id_usuario, nombre_usuario in mapeo_usuarios.items():
    print(f"ID: {id_usuario}, Usuario: {nombre_usuario}")

