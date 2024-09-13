# for y while

numero = [1,2,10,33,5,11,6,9]


for cuenta in numero:
    print("En esta linea cuenta es igual a:",++cuenta)

for cuenta in range(3,10):
    print(cuenta)

dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

for dias_semanas in dias_semana:
    print(dias_semanas)
    if dias_semanas =="Martes":
        print("Hoy es ",dias_semanas)


##while

x=0
while x <=5 :
    if x==3:
        break
    print (x)
    x = x+1