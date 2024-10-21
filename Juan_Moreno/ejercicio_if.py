## Club privado, restriccion de edad y si es o no miembro

is_miembro_club = True
edad = 11

if is_miembro_club: 
    if edad >= 18:
        print("Tiene acceso")
    else:
        print("No puede ingresar, es menor de edad")
else:
    print("No eres miembro del club y no tienes acceso")


#if edad>=18:
#    print("Tiene acceso")
#else:
#    print("No tiene acceso, es menor de edad")


print("------------------------")

x = 9
y = 20

print("====AND====")

if x > 10 and y <= 20:
    print("x > 10 & y < 20")
else:
    print("No cumple con la condicion de AND")

print("====OR====")

if x > 10 or y <= 19:
    print("x > 10 & y < 20")
else:
    print("No cumple con la condicion de OR")

print("====NOT====")

if not x > 8:
    print("x > 10")
else:
    print("No cumple con la condicion")
