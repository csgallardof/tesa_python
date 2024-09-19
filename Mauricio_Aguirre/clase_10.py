## lectura de csvs
## se utilizan librerias tipo input

import csv

with open('products.csv', mode='r') as file:
    csv_reader =csv.DictReader(file)
    for row in csv_reader:
        print(row)
        
## mostrar información por columnas

with open('products.csv', mode='r') as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(f"producto:{row['name']}, Precio:{float (row['price'])}")