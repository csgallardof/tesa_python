import os

#Directorio actual
pwd = os.getcwd()
print("la ruta donde estoy es: ",pwd)

#lista el numero de archivos csv
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
print("Archivos CSV:",csv_files)

#lista el numero de archivos txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos TXT:",txt_files)

#lista el numero de archivos py
py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print("Archivos PY:",py_files)


#renombrar
os.rename('cuento.txt', 'cuento_v2.txt')
print('Archivo')

#lista el numero de archivos txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos TXT:",txt_files)