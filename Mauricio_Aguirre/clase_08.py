### funciones

def mi_nombre(nombre, apellido="Aguirre"):
    print("hola", nombre, apellido)

mi_nombre("Mauricio")

mi_nombre(apellido="Mauricio", nombre="Flores")

### funcion de numeros primos

def es_primo(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num %i==0:
            return False
        return True

numero=223

if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")

### cadena para colocar en Mayusculas

def a_mayusculas(cadena):
    return cadena.upper()

texto = "Hola Mundo"
texto_mayusculas = a_mayusculas(texto)
print(texto_mayusculas)


### Calculadora

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Un numero no puede ser divisible en Cero"
    return a/b


num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))
print("la suma es:", suma(num1,num2))
print("la resta es:", resta(num1,num2))
print("la multiplicacion es:", multiplicacion(num1,num2))
print("la division es:", division(num1,num2))