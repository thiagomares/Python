import sqlite3 as sql
import matplotlib as plt

conector = sql.connect('Bancodedados.db')
cursor = conector.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS valores ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT',
#                'dia INTEGER',
#                'valor REAL'
#                ')')

dia = range(1, 11)
valores = [10, 2, 3, 11, 3, 4, 10, 2, 3, 5]

# for i in dia:
#     cursor.execute('INSERT INTO valores (dia, valor) VALUES (?, ?)', (dia[i], valores))

# plotagem = cursor.execute('SELECT valor FROM valores WHERE dia LIKE ?', (3))

plt.plot(dia, valores)
plt.show()

cursor.close()
conector.close()