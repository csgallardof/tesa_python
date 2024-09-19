
#### mapeo de usuarios 

Cantidad_Usuarios = int (input ("Ingrese la cantidad de Usuarios: "))


i=0
i=i+Cantidad_Usuarios

usuarios = {}

for i in range(Cantidad_Usuarios):
    
    Cedula = (input ("Ingrese su Cédula: "))
    Nombres = (input ("Ingrese sus Nombres: "))
    Apellidos = input ("Ingrese sus Apellidos: ")
    Area = input ("Ingrese su Área: ")

    usuarios[Cedula] = { "Nombres": Nombres,"Apellidos": Apellidos,"Área": Area}


# Mapeo de Usuario por cédula

consulta_cedula = input("\nIngrese la cédula para consultar la información: ")

if consulta_cedula in usuarios:

    info_usuario = usuarios[consulta_cedula]
    print(f"\nInformación del usuario:\nCédula: {consulta_cedula}\nNombres: {info_usuario['Nombres']}\nApellidos: {info_usuario['Apellidos']}\nÁrea: {info_usuario['Área']}")
else:
    print("No se encontró ningún usuario con esa cédula.")
