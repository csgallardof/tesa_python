import psycopg2

conn = psycopg2.connect(database="tesa_python_db",
                        host="155.138.253.162",
                        user="postgres",
                        password="JHEQWR2ZUASDasdgASd98x",
                        port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM pablo_miranda LIMIT 10;")

print(cursor.fetchall())

cursor.close()
conn.close()