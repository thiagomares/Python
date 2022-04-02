import sqlite3  # Importando a lib de banco de dados

conn = sqlite3.connect('basededados.db')  # Conectando com a base de dados
cursor = conn.cursor() 

cursor.execute('DELETE FROM clientes')
conn.commit()

cursor.close()
conn.close()