#### identificadores de librerias

import os ## nos permite obtener informacion del directorio actual

## directorio actual

pwd = os.getcwd()
print ("Mi directorio actual es: ", pwd)

## listar el numero de archivos csv

csv_files= [f for f in os.listdir('.') if f.endswith('.csv')]
print ("archivos csv: ", csv_files)


txt_files= [f for f in os.listdir('.') if f.endswith('.txt')]
print ("archivos txt: ", txt_files)

### renombrar archivos

os.rename('cuento.txt', 'cuento_v2.txt')
print('Archivo')

txt_files= [f for f in os.listdir('.') if f.endswith('.txt')]
print ("archivos txt: ", txt_files)


## Renombrar archivos

os.rename("cuento.txt","cuento_v2.txt")
print("archivo")


txt_files = [f for f in os.listdir("/var/www/ht1/") if f.endswith(".txt")]
print("Archivos txt", txt_files)