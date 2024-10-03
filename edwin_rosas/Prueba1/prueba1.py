import pandas as pd

# Leemos el archivo CSV, se indica el separador, el inicio de la lectura y las columnas
df = pd.read_csv('Prueba 1 Tesa.csv',sep=';',skiprows=5,usecols=['Country/Region','Country/Region Name','Approval Status'])

# funcion que agrupa por pais y cuenta la cantidad de veces que se repite un pais
def agrupar_por_pais(df):
    paises = df['Country/Region'].value_counts()
    print("Country/Region únicos:")
    for valor,cantidad in paises.items():
            print(f'{valor}: {cantidad}')

# funcion que cuenta las veces que esta en la columna "Approval Status" en estado "approved"
def contar_registros_aprobados(df):
    aprobados = df[df['Approval Status'] == 'approved']
    return len(aprobados)


def main():
    agrupar_por_pais(df)
    num_aprobados = contar_registros_aprobados(df)
    print(f"\nNúmero de registros aprobados: {num_aprobados}")


if __name__ == "__main__":
    main()



