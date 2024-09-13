#funciones


def mi_nombre(nombre, apellido = "Rosas"):
    print ("Hola",nombre,apellido)


mi_nombre("Edwin")
mi_nombre("Edwin","Yague")
mi_nombre (apellido="Yepez", nombre="Diana")


##numeros primos

def es_primo(num):
    if num<=1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ejemplo de uso
numero = 223
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")


### convertir un rango de caracteres en mayusculas

def a_mayusculas (cadena):
    return cadena.upper()

palabra = "edwin"
print (palabra, a_mayusculas(palabra))


##calculadora

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


#num1=15
#num2=3

num1= float(input("Ingrese un numero A: "))
num2= float(input("Ingrese un numero B: "))

print("La suma de", num1 ,"mas",num2,"es:",suma(num1,num2))
print("La resta de", num1 ,"menos",num2,"es:",resta(num1,num2))
print("La multiplicacion de", num1 ,"por",num2,"es:",multiplicacion(num1,num2))
print("La division de", num1 ,"entre",num2,"es:",division(num1,num2))
