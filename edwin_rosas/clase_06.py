#manejo de condicionales

##Club privado, restriccion de Edad y si es o no miembro
is_miembro_club = True 
edad = 19

if is_miembro_club:
    if edad >=18:
        print("Tiene acceso")
    else:
        print("No tiene acceso por ser menor de edad")
else:
 print("No tiene acceso por no ser miembre del club")



 #if is_miembro_club and (edad >=18):
 #      print("Tiene acceso")
#else:
# print("No tiene acceso por no ser miembre del club")

print ("----------------AND----------------")

x=9
y=21

if x>10 and y<=20:
   print("Se cumple la condicion AND, X es",x, " y Y es" ,y)
else:
   print("no cumple la condición AND")



print ("---------------OR-----------------")


if x>10 or y<=20:
   print("Se cumple la condicion OR, X es",x, " y Y es" ,y)
else:
   print("no cumple la condición OR")


print ("---------------NOT-----------------")

if not x>10:
   print("Se cumple la negacion de X, X es",x, " y Y es" ,y)
else:
   print("no cumple la condición NOT")
