
#Club Privadoreestriccion de eddad y si es o no miembro

is_miembro_club = False

edad = 11

#primera condicional

if is_miembro_club:
    if edad >=18:
       print ("Tiene acceso")
    else:
     print ("No tiene Acceso Menor de edad")
else:
   print("No eres miembro del club y no tiene acceso")


#if edad >=18:
 #       print ("Tiene acceso")
  #  else:
   #     print ("No tiene Acceso Menor de edad")


print("----------------------")

x = 9
y = 20

if x>10 and y<=20:
   print("X > 10 y Y < 20")
else:
   print ("No cumple con la condición AND")


print("----------OR------------")


if x>10 or y<=19:
   print("X > 10 y Y < 20")
else:
   print ("No cumple con la condición OR")


print("---------NOT------------")

if not x>8: 
   print("X > 10 y Y < 20")
else:
   print ("No cumple con la condición NOT")
