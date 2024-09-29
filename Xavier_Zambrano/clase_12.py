###Busqueda, Identifiación, modificación de tipos de archivos (txt,py,json,dll)

import os   #Libreria para obtener la información de un directorio

##Directorio Actual##

pwd = os.getcwd()
print("Mi directorio actual es: ", pwd)

##contabilizar el numero de archivos por tipo por lista

csv_files = [f for f in os.listdir('.') if f.endswith('csv')]
print("Archivos csv: ",csv_files)

txt_files = [f for f in os.listdir('.') if f.endswith('txt')]
print("Archivos txt: ",txt_files)

##Renombrar un archivo

os.rename('cuento.txt', 'cuento_v2.txt')
print("Archivo Modificado")

txt_files = [f for f in os.listdir('.') if f.endswith('txt')]
print("Archivos txt: ",txt_files)
