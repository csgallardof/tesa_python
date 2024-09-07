#Mapeo de usurios

id_usuario = int(input ("Digite el numero del usuario: "))

usuarios = {
    1: {"nombre": "Josue", "edad": 24, "correo": "josue@example.com"},
    2: {"nombre": "Edwin", "edad": 30, "correo": "edwin@example.com"},
    3: {"nombre": "Carlos", "edad": 32, "correo": "carlos@example.com"}
}

if id_usuario in usuarios:
    print("Nombre: {}".format(usuarios[id_usuario]['nombre']))
    print("Edad: {}".format(usuarios[id_usuario]['edad']))
    print("Correo: {}".format(usuarios[id_usuario]['correo']))
else:
    print("Usuario no encontrado")
