import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV en un DataFrame
file_path = 'C:/Users/Reowo/tesa_python/Juan_Moreno/Semana_Comex_USA_Jul_2024.csv'  # Usa la ruta absoluta
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Información general sobre el DataFrame
print("\nInformación general:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Encontrar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Eliminar filas con valores nulos
df = df.dropna()
print("\nDataFrame después de eliminar filas con valores nulos:")
print(df.head())

# Análisis de datos (ejemplo: agrupación y suma)
# Agrupando por 'Country/Region' y contando los registros
registros_por_pais = df.groupby('Country/Region').size()
print("\nRegistros por País:")
print(registros_por_pais)

# Encontrar los 10 países con más registros
top_10_paises = registros_por_pais.nlargest(10)
print("\nTop 10 Países con más registros:")
print(top_10_paises)

# Visualización de datos
# Gráfico de barras de registros por país
registros_por_pais.plot(kind='bar', figsize=(10, 6))
plt.title('Registros por País')
plt.xlabel('País')
plt.ylabel('Cantidad de Registros')
plt.xticks(rotation=45)
plt.show()

# Gráfico de los 10 países con más registros
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_paises.values, y=top_10_paises.index, palette='viridis')
plt.title('Top 10 Países con Más Registros')
plt.xlabel('Cantidad de Registros')
plt.ylabel('País')
plt.show()
