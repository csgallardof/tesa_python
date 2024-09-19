### lectura de csv

import csv

# with open('products.csv',mode='r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)


#Mostrar la informcion por columnas
with open('products.csv',mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print (f"Marca:{row['brand']}, Precio:{float(row['price'])}")