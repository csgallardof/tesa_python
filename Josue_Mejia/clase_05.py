#### Diccionarios se representan con {:}

numeros={1:"Uno", 2:"dos", 3:"tres"}

## para acceder utilizamos la siguiente forma

print(numeros[3])

### guardar en el diccionario la informacion personal

informacion_personal = {"Nombre":"Josue",
                       "telefono":"099002302",
                       "email":"josuemejiav@hotmail.com"}
print(informacion_personal["Nombre"])

### las claces de los diccionarios son los argumentos antes de los : por medio del keys

claves = informacion_personal.keys()
print(claves)


## para imprimir los valores que estan luego del : que son los valores entregados por medio del values

valores = informacion_personal.values()
print(valores)

## para imprimir todos los elementos del diccionario lo hacemos mediante el items

elementos=informacion_personal.items()
print(elementos)


### configuracion de aplicaciones

config = {"host": "localhost",
          "port": 8080,
          "title": "Mi PRIMERA APLICACION"
          }
print("Configuracion de mi primera aplicacion", config)


