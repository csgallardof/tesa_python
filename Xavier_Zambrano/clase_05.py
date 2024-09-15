print("Configuracion de mi primera APP", config)

# contador de palabras dentro de un diccionario

palabras = {"Saludo":"Hola Edwin"
"Color":"Verde",
"Pals":"Ecuador"
"Marcr":"Volkswagen Escarbajo blanco"
"Peso": "Kilos"}

cantidad_palabras = 0

print(palabras.items())
for clave, valordeclave in palabras.items():
cuenta_palabras = len(valordeclave.split()) #len es el numero de elementos y split divide una cadena en una lista
cantidad_palabras += cuenta_palabras #aqui se suma


print("Cantidad de palabras que tienen los valores del diccionario palabras:", cantidad_palabras)