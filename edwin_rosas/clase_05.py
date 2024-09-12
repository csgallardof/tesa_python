##diccionarios
## se representa con llaves {}
nummeros ={1:"Uno",2:"Dos",3:"Tres",10:"Diez"}

print(nummeros[3])
print(nummeros[10])

informacion_personal ={"nombre":"Edwin",
                       "apellido":"Rosas",
                       "telefono":"0986805369",
                       "email":"erosas@estud.tesa.edu.ec"}

print(informacion_personal["nombre"])

##claves

claves= informacion_personal.keys()
print(claves)

##valores
valores = informacion_personal.values()
print(valores)

##elementos
elementos = informacion_personal.items()
print(elementos)

## configuracion aplicaciones

config = {"host":"localhost",
          "port":8080,
          "title":"Mi primera APP"
          }

print("Configuracion de mi primera APP",config)


# contador de palabras dentro de un diccionario

palabras = {"Saludo":"Hola Edwin",
            "Color":"Verde",
            "Pais":"Ecuador",
            "Marca":"Volkswagen Escarbajo blanco",
            "Peso": "Kilos"}


cantidad_palabras = 0

print(palabras.items())
for clave, valordeclave in palabras.items():
        cuenta_palabras = len(valordeclave.split())  #len es el numero de elementos y split divide una cadena en una lista
        cantidad_palabras += cuenta_palabras #aqui se suma
        

print("Cantidad de palabras que tienen los valores del diccionario palabras:",cantidad_palabras)

# mapeo de usuarios 

lista_usuario = ["usuario1","usuario2"]
lista_nombre = {"usuario1":"Edwin", "usuario2":"Leonardo"}

for mapeousuario in lista_usuario:
    if mapeousuario in lista_nombre.keys():
        print("Nombre: ", lista_nombre[mapeousuario])
    else:
        print("no existe usuario")



