import psycopg2

# Parámetros de conexión
hostname = '155.138.253.162'     # Dirección IP o hostname del servidor remoto
database = 'tesa_python_db'   # Nombre de la base de datos
username = 'postgres'        # Nombre de usuario de la base de datos
password = 'JHEQWR2ZUASDasdgASd98x'        # Contraseña de la base de datos
port = '5432'                     # Puerto, generalmente 5432 para PostgreSQL

try:

    connection = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=password,
        port=port
    )
   
    # Crear cursor para ejecutar consultas
    cursor = connection.cursor()

    # Ejecutar una consulta
    query = "SELECT * FROM semana_comex_usa_jul;"  # Ajusta la consulta a tus necesidades
    cursor.execute(query)

    # Obtener los resultados
    records = cursor.fetchall()

    # Mostrar los resultados
    for row in records:
        print(row)

    # Cerrar cursor y conexión
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error al conectar a la base de datos: {error}")