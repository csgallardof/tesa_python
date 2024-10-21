# Una disculpa profe, ha sido difícil con los cortes de luz. Estoy subiendo la prueba con datos. Me pondré al día con el resto esta misma semana

import pandas as pd

def agrupar_por_pais(df):
    
    agrupado_pais = df.groupby('Country/Region Name').size()
    return agrupado_pais

def contar_aprobados(df):
    
    num_aprobados = df[df['Approval Status'] == 'approved'].shape[0]
    return num_aprobados

def cargar_csv(ruta_csv):
    
    df = pd.read_csv(ruta_csv, skiprows=5, delimiter=';')
    return df

def main():
    ruta_csv = 'Prueba 1 Tesa.csv'  
    df = cargar_csv(ruta_csv)

   
    agrupado_pais = agrupar_por_pais(df)
    print("Registros agrupados por país:\n", agrupado_pais)

    
    num_aprobados = contar_aprobados(df)
    print("\nNúmero de registros aprobados:", num_aprobados)

if __name__ == "__main__":
    main()
