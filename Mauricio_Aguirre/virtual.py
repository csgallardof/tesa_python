# Ejemplo de conexión con psycopg2
import psycopg2

# Datos de conexión
conn = psycopg2.connect(
    database="mi_base_datos",
    user="mi_usuario",
    password="mi_contraseña",
    host="localhost",
    port="5432"
)

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM mi_tabla")

# Obtener los resultados
resultados = cursor.fetchall()

# Cerrar la conexión
cursor.close()
conn.close()

# Manejo de archivos CSV y XLS:

import csv

with open('mi_archivo.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        # Procesar cada fila
        print(fila)
        
#XLS (con openpyxl):

import openpyxl

workbook = openpyxl.load_workbook('mi_archivo.xlsx')
hoja = workbook.active

# Acceder a los datos de la hoja
for fila in hoja.iter_rows(values_only=True):
    print(fila)
    