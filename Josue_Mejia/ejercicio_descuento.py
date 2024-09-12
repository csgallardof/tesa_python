
edad = int(input("Digame su edad: "))
tipo_de_carnet = input("Digame su tipo de carnet (E para estudiante / P Pensionista / F Familia numerosa / N Nada) ")

if (edad <= 35 and edad >= 25 and tipo_de_carnet == "E") or \
        edad <= 10 or \
        (edad >= 65 and tipo_de_carnet == "P") \
        or(tipo_de_carnet == "F"):
    print("Se te aplica el descuento")
else:
    print("No se te aplica el descuento")