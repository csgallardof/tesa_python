
#### funciones

def mi_nombre(nombre, apellido="Gallardo"):
    print("Hola", apellido, nombre)

mi_nombre("Carlos","Flores")

mi_nombre(apellido="Cespedes",nombre="Santiago")


### Numero primos

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num %i == 0:
            return False
    return True


numero = 223
if es_primo(numero):
    print(numero, "es primo ")
else:
    print(numero, "no es primo")


##### Mayusculas

def a_mayusculas(cadena):
    return cadena.upper()

texto = "Hola mundo"
texto_mayusculas = a_mayusculas(texto)
print(texto_mayusculas)



#### Calculadora

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplication(a,b):
    return a*b

num1 = float(input("ingrese un numero A: "))
num2 = float(input("ingrese un numero B: "))

print("la suma es: ", suma(num1,num2))
