
print("\nDictionaries")

test = {"uno":1, "dos":2, "tres":3}

print("\nItems -> ", test.items())
print("\nKeys -> ", test.keys())
print("\nValues -> ",test.values())

print("\n")
print(test)
print(test["dos"])

print("\nContador de palabras dentro de un diccionario")
diccionario = ["doubt",1,"mind","drive",2,"implication",{1:2},"brink","ratio","album","tune"]

count = 0
for item in diccionario:
    if isinstance(item, str):
        count += 1

print(diccionario)
print("Count: ", count)

print("\nMapeo de usuarios")
usuarios = ["usuario1","usuario2","usuario3","usuario4","usuario5"]
nombres = {"usuario1":"Angel", "usuario3":"Pedro", "usuario6":"Paul"}

for usuario in usuarios:
    if usuario in nombres.keys():
        print("Nombre: ", nombres[usuario])
    else:
        print("no existe")