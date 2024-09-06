#### Diccionarios se representan con {:}

numeros={1:"Uno", 2:"dos", 3:"tres"}

## para acceder utilizamos la siguiente forma

print(numeros[3])

### guardar en el diccionario la informacion personal

informacion_personal = {"Nombre":"Mauricio", 
                       "telefono":"0980192028", 
                       "email":"appsandplays@hotmail.com"}
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

## Contador de palabras dentro de un Diccionario
def contar_palabras_de_un_diccionario(diccionario):
  # Creamos una variable para el conteo y que nos muestre el total
  contador_palabras = {}
  total_palabras = 0

  # creamos el for para que realice el conteo
  for valor in diccionario.values():
      # Verificamos si el valor es una lista o una cadena
      if isinstance(valor, list):
          # Si es una lista, iteramos sobre cada elemento (que asumimos es una cadena)
          for palabra in valor:
              contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
              total_palabras += 1
      elif isinstance(valor, str):
        # Si es una cadena, la dividimos en palabras          
          for palabra in valor.split():
                contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
                total_palabras += 1  
  # Agregamos el total de palabras al diccionario
  contador_palabras['total'] = total_palabras

  return contador_palabras
### Ejecucion
mi_diccionario = {
    "usuario1": ["Hola", "Bienvenido", "Como", "Estas","es","un","placer","Conocerte"]
}

resultado = contar_palabras_de_un_diccionario(mi_diccionario)
print(resultado)

## Mapeos de usuarios

usuarios = {
    "usuario1": {
        "nombre": "Juan Pérez",
        "edad": 30,
        "ciudad": "Madrid",
        "intereses": ["programación", "música", "viajar"]
    },
    "usuario2": {
        "nombre": "Ana García",
        "edad": 25,
        "ciudad": "Barcelona",
        "intereses": ["lectura", "cine", "deportes"]
    }
}

print(usuarios["usuario1"]["nombre"])  
print(usuarios["usuario2"]["intereses"])