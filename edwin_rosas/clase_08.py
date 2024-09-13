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
    try:
        return a/b
    except ZeroDivisionError:
        return "Un número no puede ser divisible en Cero"
    


#num1=15
#num2=3

num1= float(input("Ingrese un número A: "))
num2= float(input("Ingrese un número B: "))

# Menú de operaciones
print("\nSeleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
    
opcion = input("Elija una opción (1/2/3/4): ")

if opcion =="1":
    print("La suma de", num1 ,"mas",num2,"es:",suma(num1,num2))
elif opcion =="2":
    print("La resta de", num1 ,"menos",num2,"es:",resta(num1,num2))
elif opcion =="3":
    print("La multiplicación de", num1 ,"por",num2,"es:",multiplicacion(num1,num2))
elif opcion =="4":
    print("La división de", num1 ,"entre",num2,"es:",division(num1,num2))
else:
    print("opción no valida")
