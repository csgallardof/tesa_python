#Conteo de palabras

total_palabras = 0

diccionario = {
    1: "programar",
    2: "python",
    3: "consola",
}

for clave in diccionario:
    total_palabras += 1  # Cada entrada en el diccionario cuenta como una palabra

print("El número total de palabras es: {}".format(total_palabras))