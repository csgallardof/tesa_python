### lectura de csv
## se debe verificar que este instalado 
import csv
import operator

with open('tesa_python/edwin_rosas/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)


##mostrar la informacion por columnas

with open('tesa_python/edwin_rosas/products.csv', mode='r') as file:
    csv_reader= csv.DictReader(file)
    ##crear variable para ordenar por una columna del CSV, reverse false es A-Z y true es Z-A
    rows = sorted(csv_reader, reverse=False, key=operator.itemgetter('name'))
    for row in rows:
        print(f"Producto:{row['name']},Marca:{row['brand']},Precio:{float(row['price'])}")


