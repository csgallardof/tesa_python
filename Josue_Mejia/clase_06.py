## Club privado, reestriccion de edad y si es o no miembro
is_miembro_club = False
edad = 18

if is_miembro_club:
    if edad>=18:
        print("Tiene acceso")
    else:
        print("Señor usuario usted no tiene acceo ")
else:
    print("NO eres miembro del club y no tienes acceso")

# if edad>=18:
#     print("Tiene acceso")
# else:
#     print("Señor usuario usted no tiene acceo ")



print("----AND-------")


x = 9
y = 20

if x>10 and y<=20:
    print("x > 10 y Y < 20")
else:
    print("no cumple con la condicion AND")



print("-----OR-----")

if x>10 or y<=19:
    print("x > 10 y Y < 20")
else:
    print("no cumple con la condicion OR")


print("-----NOT-----")

if not x>8:
    print("x > 10 y Y < 20")
else:
    print("no cumple con la condicion NOT")