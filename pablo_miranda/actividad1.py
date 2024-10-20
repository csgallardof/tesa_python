
import statistics
import csv

print("Ventas Mensuales")

ventas_mensuales = {}

with open("monthly_sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row['month']
        sales = int(row['sales'])

        ventas_mensuales[month] = sales

sales = list(ventas_mensuales.values())

print(sales)
