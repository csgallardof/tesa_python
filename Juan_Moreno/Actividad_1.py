import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/Reowo/tesa_python/Juan_Moreno/Semana_Comex_USA_Jul_2024.csv'  # Usa la ruta absoluta
df = pd.read_csv(file_path)


print("Primeras filas del DataFrame:")
print(df.head())


df.columns = ['First Name', 'Last Name', 'Email', 'Country/Region', 'Industry', 'Registration Time',
              'Approval Status', 'Género', 'Plataforma ConnectAmericas', 'País', 'Source Name']

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())


df = df.dropna(subset=['Country/Region', 'Industry'])
print("\nDataFrame después de eliminar filas con valores nulos en 'Country/Region' e 'Industry':")
print(df.head())


registros_por_pais = df.groupby('Country/Region').size()
print("\nRegistros por País:")
print(registros_por_pais)


top_10_paises = registros_por_pais.nlargest(10)
print("\nTop 10 Países con más registros:")
print(top_10_paises)

registros_por_pais.plot(kind='bar', figsize=(10, 6))
plt.title('Registros por País')
plt.xlabel('País')
plt.ylabel('Cantidad de Registros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_paises.values, y=top_10_paises.index, palette='viridis')
plt.title('Top 10 Países con Más Registros')
plt.xlabel('Cantidad de Registros')
plt.ylabel('País')
plt.tight_layout()
plt.show()
