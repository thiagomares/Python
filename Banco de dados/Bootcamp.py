import sqlite3 as sql


conector = sql.connect('DataBase.db')
cursor = conector.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS usuários ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT',
               'username TEXT',
               'posição TEXT',
               'privilegio TEXT'
               ')')

cursor.execute('CREATE TABLE IF NOT EXISTS contas ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT',
               'username TEXT'
               'tipoGasto TEXT',
               'Valor REAL',
               'DataDebito TEXT',
               'motivo TEXT'
               ')')


valor = input('Insira o valor gasto')
username = input('Insira o usuário')
tipoGasto = input('Insira o tipo de gasto')
dataDebito = input('Insira a data do Gasto')

if tipoGasto != 'outros':
    cursor.execute('INSERT INTO contas (username, tipoGasto, Valor, DataDebito) VALUES  (?, ?, ?, ?)', (username, tipoGasto, valor, dataDebito))

if tipoGasto == 'outros':
    motivo = input('Digite o motivo do gasto')
    cursor.execute('INSERT INTO contas (username, tipoGasto, Valor, DataDebito, motivo) VALUES  (?, ?, ?, ?, ?)', (username, tipoGasto, valor, dataDebito, motivo))
    

valores = cursor.execute('SELECT valor FROM contas WHERE (username, tipoGasto LIKE (?, ?)' (username, tipoGasto))
media = sum(valores) / len(valores)

print(media)