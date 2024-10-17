import os 

## Directorio actual 

pwd= os.getcdw()

print ("Mi directorio actual es: ", pwd)

## Listar el numero de archivos csv

csv_files= [f for f in os.listdir('.') if f.endswith('.csv')]
