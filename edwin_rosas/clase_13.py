#librerias matematicas y randomico

import math
import random

radio = 10
area = math.pi*radio**2
print ("El area de un circulo con radio de",radio,"es :",area)

#perimetro
perimetro= 2*math.pi*radio
print ("El perimetro de un circulo con radio de",radio,"es :",round(perimetro,2))


###generar un numero aleatorio

num_random = random.randint(20,30)
print(num_random)

colors =['azul','rojo','verde']
random_color= random.choice(colors)
print(random_color)