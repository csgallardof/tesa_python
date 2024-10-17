### funciones

def mi_nombre(nombre, apellido="Moreno"):
    print("Hola", nombre, apellido)

mi_nombre("Juan", "Moreno")
mi_nombre(apellido="Ocampo", nombre="Sebastian")

## Numeros primos

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

numero = 223

if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")

## Mayusculas

def a_mayusculas(cadena):
    return cadena.upper()

texto = "q fue"
texto_mayus = a_mayusculas(texto)
print(texto_mayus)

## Calculadora

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

print("La suma es:", suma(num1, num2))
print("La resta es:", resta(num1, num2))
print("La multiplicacion es:", multiplicacion(num1, num2))
print("La division es:", division(num1, num2))






