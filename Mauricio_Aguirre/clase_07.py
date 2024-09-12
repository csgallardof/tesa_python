### for bucles de repeticion

print("------------for------------------")
numero=[1,2,3,4,5,6,7,8,9,10]

i=0
for i in numero:
    print("En esta línea i es igual a: ", ++i)
    
for i in range(3,10):
    print(i)


print("------------FOR AND IF------------------")
    
dias_de_la_semana=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

for dias_de_la_semanas in dias_de_la_semana:
    print(dias_de_la_semanas)
    if dias_de_la_semanas == "martes":
        print("dia encontrado")

print("------------while------------------")
x=0

while x<5:
    if x==3:
        break
    print(x) 
    
    x+=1  
        
