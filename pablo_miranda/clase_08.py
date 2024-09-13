
print("Funciones")

def func_example():
    print("\nHola Mundo")

def func_saludo(nombre, apellido):
    print("\nHola ", nombre, apellido)

def is_prime(num):
    a = 0
    for i in range(1, num):
        if num % i == 0:
            a += 1

    if a == 2:
        print(num, "es primo")
    else:
        print(num, "no es primo")


func_example()
func_saludo("Pablo", "Miranda")

is_prime(15)