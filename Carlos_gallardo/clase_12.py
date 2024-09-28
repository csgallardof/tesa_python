import os

#Directorio actual 
pwd = os.getcwd()
print ("Mi directorio actua es: ", pwd)


#Listar el numero de archivos csv

csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
print("Archivos csv:", csv_files)



txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos csv:", txt_files)


## Renombrar un archivo
# os.rename('cuento.txt', 'cuento_v2.txt')
# print('Archivo')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)


## Renombrar un archivo
os.rename('cuento_v2.txt', 'cuento_v3.txt')
print('Archivo')


txt_files = [f for f in os.listdir('/var/www/htl/') if f.endswith('.txt')]
print("Archivos txt:", txt_files)