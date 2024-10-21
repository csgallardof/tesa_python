# Análisis de datos utilizando la librería pandas, el data source será recolectado desde fuentes públicas.


import pandas as pd
import requests


url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-summary-of-the-month&startDate=1880-01-01&endDate=2023-12-31&dataTypes=sst&format=json"

# Realizar la petición HTTP
response = requests.get(url)
data = response.json()

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(data['results'])

# Convertir la columna 'time' a formato datetime
df['time'] = pd.to_datetime(df['time'])

# Explorar los primeros registros
print(df.head())

# Resumen estadístico
print(df.describe())

# Gráfico de la temperatura promedio global a lo largo del tiempo
df.plot(x='time', y='sst', kind='line', title='Temperatura superficial del mar global')

# Calcular la temperatura promedio por año
df['year'] = df['time'].dt.year
temp_por_año = df.groupby('year')['sst'].mean()

# Identificar el año más cálido y el más frío
año_mas_calido = temp_por_año.idxmax()
año_mas_frio = temp_por_año.idxmin()
print(f"El año más cálido fue {año_mas_calido} con una temperatura promedio de {temp_por_año[año_mas_calido]}")
print(f"El año más frío fue {año_mas_frio} con una temperatura promedio de {temp_por_año[año_mas_frio]}")

# Visualizar la tendencia de la temperatura a largo plazo
temp_por_año.plot(kind='line', title='Evolución de la temperatura superficial del mar')