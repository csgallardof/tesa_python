
##Conteo de Palabras


print("Ingrese la siguiente información","\n")

Nombre = (input ("Ingrese su nombre: "))
Telefono = (input ("Ingrese su teléfono: "))
Email = input ("Ingrese su Email: ")

informacion_personal = {"Nombre": Nombre ,"Teléfono": Telefono, "email":Email} 

conteo = 0

for items in informacion_personal.values():
    
    palabras = len(items.split())
    conteo += palabras

print("Cantidad de palabras ingresadas son: ", conteo) 
