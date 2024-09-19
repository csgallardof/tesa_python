import statistics
import csv
import operator

ventas_mensuales={}

with open('tesa_python/edwin_rosas/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    ##para ordenar la columna sales del csv
    rows = sorted(reader, reverse=False, key=operator.itemgetter('sales'))
    for row in rows: ## reader
        mes = row['month']
        ventas = float(row['sales'])
        
        ventas_mensuales[mes]=ventas

ventas= list(ventas_mensuales.values())
print(ventas)

##calculo de media estadistica
total_ventas = statistics.mean(ventas)
print (f"La media es :{round(total_ventas,2)}")

##calculo de la mediana estadistica
total_ventas = statistics.median(ventas)
print (f"La mediana es :{round(total_ventas,2)}")

##calculo de la moda estadistica
total_ventas = statistics.mode(ventas)
print (f"La moda es :{total_ventas}")

##calculo de la varianza estadistica
total_ventas = statistics.variance(ventas)
print (f"La varianza es :{round(total_ventas,2)}")

##calculo de la maximo estadistica

print (f"La maxima es :{max(ventas)}")

##calculo del minimo estadistica
print (f"La minima es :{min(ventas)}")

##calculo del rango estadistica
rango_ventas = max(ventas)-min(ventas)
print (f"El rango es :{rango_ventas}")
print (f"El rango opcion2 es :{max(ventas)-min(ventas)}")