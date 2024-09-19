#### Diccionarios (Estructuras de datos clave\valor)

numeros = {1:"Uno",2:"dos",3:"tres"}
print(numeros[3])
      
informacion_personal = {"Nombre": "Xavier","Teléfono": "0998872275", "email":"computerskx@gmail.com"} 
print(informacion_personal["Nombre"])

claves =informacion_personal.keys()  ## se puede acceder o extraer las claves con keys
print(claves)

valores = informacion_personal.values() ## se puede acceder o extraer los valores con value
print(valores)

elementos = informacion_personal.items() ## se puede acceder o extraer las claves y valores con items
print(elementos)

##Configuracion de aplicacion

config = {"host": "LocalHost","Port":8080,"Title":"Mi Primera Aplicación"}

print("Configuración de mi Primera Aplicación",config)
