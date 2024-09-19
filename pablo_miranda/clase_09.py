
print("Manejo de archivos")

with open("cuento.txt", "r") as file:
    print("Lines: ", len(file.readlines()))
