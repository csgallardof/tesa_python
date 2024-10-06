### funciones matematicas básicas

import math ## para operaciones matematicas
import random ## numeros aleatorios de rangos

### identificar el area de un circulo

radio=10
area = math.pi * radio**2
print (area)

### identificar el area de un circulo

perimetro= 2*math.pi*radio
print(perimetro)

## generar numero aleatorio con ramdom

num_random =  random.randint(20,30) ## randin nos devuelve un numero entero entre los valores asignados
print(num_random)

colors = ['azul','rojo','verde']
random_color = random.choices(colors)## choices nos devuelve un valor de una lista entregada
print(random_color)