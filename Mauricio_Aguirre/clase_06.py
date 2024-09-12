### Club privado, restriccion de edad y si es o no miembro

is_miembro_club = True
edad=11

if is_miembro_club:
    if edad>=18:
        print("Tiene acceso")
    else:
        print("Señor usuario usted no tiene acceso")
else:
    print("No eres miembro del club y no tienes acceso")

#if edad>=18:
#    print("Tiene acceso")
#else:
#    print("Señor usuario usted no tiene acceso")

print ("----------------------------------------")

x=30
y=20

if  x>10 and y<=20:
    print("x > 10 y Y >20")
else:
    print("no comple con la condicion AND")

print("---------------OR--------------")

if  x>10 or y<=20:
    print("x > 10 y Y >20")
else:
    print("no comple con la condicion OR")

print("---------------NOT--------------")

if  not x>10:
    print("x > 10 y Y >20")
else:
    print("no comple con la condicion NOT")