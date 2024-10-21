import pandas as pd

df = pd.read_csv('productos_nuevos.csv')

# Mostrar los primeros 5 registros
print("Datos originales:")
print(df.head())

# Calcular el total de ventas (unidades) y total en ingresos (Ventas * Precio)
df['Total_Ventas'] = df['Ventas'] * df['Precio']

print("\nDatos con total de ventas calculado:")
print(df)

# Estadísticas básicas
print("\nEstadísticas generales:")
print(df.describe())

# Filtrar productos con ventas mayores a 10 unidades
ventas_mayores_10 = df[df['Ventas'] > 10]
print("\nProductos con ventas mayores a 10 unidades:")
print(ventas_mayores_10)