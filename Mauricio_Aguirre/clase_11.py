### importar archivos y realizar operacines matematicas
### calculo de media, mediana, moda, variaza, etc
import statistics
import csv


ventas_mensuales={}

with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        ventas_mensuales[month]=sales
    
sales = list(ventas_mensuales.values())
print(sales)

## calculo de media

total_sales = statistics.mean(sales)
print(f"La media es: {total_sales}")

## calculo de mediana

total_sales = statistics.median(sales)
print(f"La mediana es: {total_sales}")


## calculo de moda

total_sales = statistics.mode(sales)
print(f"La moda es: {total_sales}")


## calculo de varianza

total_sales = statistics.variance(sales)
print(f"La varianza es: {total_sales}")


### maxima y minimda

max_sales= max(sales)
print(max_sales)

min_sales= min(sales)
print(min_sales)

rango_sales= max_sales - min_sales
print(f'Rango de ventas: {rango_sales}')