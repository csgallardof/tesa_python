import pandas as pd


url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(url)

# Agrupar por país y calcular los promedios
promedios_por_pais = df.groupby('Country').agg({
    'Confirmed': 'mean',
    'Recovered': 'mean',
    'Deaths': 'mean'
}).round(2)  # Redondear a 2 decimales para mejor legibilidad

# Renombrar columnas
promedios_por_pais.columns = ['Promedio Confirmados', 'Promedio Recuperados', 'Promedio Muertes']

# Ordenar
promedios_por_pais = promedios_por_pais.sort_values('Promedio Confirmados', ascending=False)

# resultados
print(promedios_por_pais)

