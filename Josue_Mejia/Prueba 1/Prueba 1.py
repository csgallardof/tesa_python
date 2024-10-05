import pandas as pd

def main():
    file_path = 'C:\\Users\\DELL\\Desktop\\Documentos Ins\\Segundo Semestre\\Python\\tesa_python\\Josue_Mejia\\Prueba 1\\Prueba 1 Tesa.csv'

    # Cargar datos
    datos = pd.read_csv(file_path, sep=';', skiprows=5, usecols=['Country/Region', 'Approval Status'])

    # Conteo de registros por país
    print("Conteo de registros por Country/Region:")
    for pais, cantidad in datos['Country/Region'].value_counts().items():
        print(f'{pais}: {cantidad}')

    # Contar y mostrar registros aprobados
    total_aprobados = (datos['Approval Status'].str.lower() == 'approved').sum()
    print(f"\nNúmero total de registros aprobados: {total_aprobados}")

if __name__ == "__main__":
    main()
