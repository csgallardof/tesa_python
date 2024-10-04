

##Lectura de datos total de caracteres en la linea

#with open('Archivos/cuento.txt','r') as file:
#    Lineas = file.readline()
#    print(len(Lineas))

#Escritura de datos se modifica el archivo adicionando el texto que se desee

#with open('Archivos/cuento.txt', 'a') as file:
#    file.write("\n hola")

#Modificación de datos se modifica el archivo borrando todo el contenido y se adicionando el texto que se desee
with open('Archivos/cuento.txt', 'w') as file:
    file.write("\n hola planeta de dos mundos")


