import pandas as pd
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
import seaborn as sns


try:
    conn = mysql.connector.connect(
        host='localhost',
        database='deberes',
        user='root',
        password=''  # No tiene clave
    )
    if conn.is_connected():
        print('Conexión exitosa a la base de datos MySQL')

        cursor = conn.cursor()

        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS deberes_general (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            descripcion TEXT,
            estado VARCHAR(50)
        )
        """)
        conn.commit()

       
        cursor.execute("""
        INSERT INTO deberes_general (titulo, descripcion, estado)
        VALUES
        ('Matemáticas', 'Resolver problemas del libro', 'pendiente'),
        ('Historia', 'Leer el capítulo 4 y 5', 'completado'),
        ('Ciencias', 'Proyecto del sistema solar', 'pendiente')
        """)
        conn.commit()

        
        query = "SELECT * FROM deberes_general;"
        df = pd.read_sql(query, conn)

        
        print(df)

       
        df.to_csv('deberes.csv', index=False)

        df_csv = pd.read_csv('deberes.csv')

        df_csv.to_excel('deberes.xlsx', index=False)

   
        df_xlsx = pd.read_excel('deberes.xlsx')

        
        print(df_xlsx.info())
        print(df_xlsx.describe())

        print(df_xlsx.isnull().sum())

    
        df_xlsx = df_xlsx.dropna()

       
        deberes_por_estado = df_xlsx.groupby('estado').size()
        print(deberes_por_estado)

      
        deberes_por_estado.plot(kind='bar')
        plt.title('Deberes por Estado')
        plt.xlabel('Estado')
        plt.ylabel('Cantidad de Deberes')
        plt.show()

except Error as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    if conn.is_connected():
        conn.close()
        print('Conexión a MySQL cerrada')
