#for

numero = [1,2,10,33,5,11,6,9]
i = 0
for i in numero:
    print("En esta linea i es igual a: {}" .format(++i))

for i in range(3,10):
    print(i)

for i in numero:
    if i == 2:
        print("dos encontrado")


dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for dias_semanas in dias_semana:
    print(dias_semanas)
    if dias_semanas == "Martes":
        print("Martes encontrado")


#while

x=0
while x<5:
    if x == 3:
        break
    print(x)
    x+=1