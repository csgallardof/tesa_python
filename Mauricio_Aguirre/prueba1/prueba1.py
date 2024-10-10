import pandas as pd

# Cargar los datos del CSV
df = pd.read_csv('Prueba 1 Tesa.csv', sep=';', skiprows=5, usecols=['Country/Region', 'Country/Region Name', 'Approval Status'])

print("Vista previa de los primeros datos:")
print(df.head())

# Función para agrupar por país y mostrar detalles
def agrupar_por_pais(df):
    # Agrupación por "Country/Region" con sus nombres
    paises = df.groupby(['Country/Region', 'Country/Region Name']).size().reset_index(name='Cantidad')
    
    print("\nRegistros agrupados por País/Región:")
    for index, row in paises.iterrows():
        print(f'Código País/Región: {row["Country/Region"]}, Nombre: {row["Country/Region Name"]}, Cantidad de registros: {row["Cantidad"]}')

# Función para contar los registros aprobados
def contar_registros_aprobados(df):
    # Normalizamos el texto del campo 'Approval Status' para evitar problemas con mayúsculas/minúsculas
    df['Approval Status'] = df['Approval Status'].str.strip().str.lower()
    aprobados = df[df['Approval Status'] == 'approved']
    return len(aprobados)

# Función principal que organiza la ejecución del programa
def main():
    agrupar_por_pais(df)
    num_aprobados = contar_registros_aprobados(df)
    print(f"\nNúmero total de registros aprobados: {num_aprobados}")

# Verificar si este archivo es el archivo principal que se está ejecutando
if __name__ == "__main__":
    main()
