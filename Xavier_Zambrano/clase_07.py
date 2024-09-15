###for

numero = [1,2,10,33,5,11,6,9]

i=0 # con esto se setea o se coloca en 0
for i in numero:
    print ("En esta linea i es igual a:", ++i)

    for i in range (3,10):
        print(i)

dias_semana = ["Lunes", "Martes", "Miercoles","Jueves","Viernes","Sabado","Domingo"]

for dias_semanas in dias_semana:
    print(dias_semanas)
    if dias_semanas == "Martes":
        print("Martes enconrado")

##bucle infinto
#x=0
#while x<5:
#    print(x)

x=0
while x<5:
    
    if x ==3:
        break
    print(x)
    x+=1       