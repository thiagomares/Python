import sqlite3  # Importando a lib de banco de dados

conn = sqlite3.connect('basededados.db')  # Conectando com a base de dados
cursor = conn.cursor()  # Esse carinha que vai fazer os comandos SQL na DB

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               # O comando 'if not exists' só vai criar a tabela se ela nao existir, entao podemos declarar direto
               'id INTEGER PRIMARY KEY AUTOINCREMENT, '
               'nome TEXT,'
               'peso REAL'
               ')')

dicionario = [
    {'nome': 'Thiago', 'peso': 98.5},
    {'nome': 'Ana Clara', 'peso': 56},
    {'nome': 'Gustavo', 'peso': 78.5}
]

nomes = list(map(lambda names: names['nome'], dicionario))
pesos = list(map(lambda weights: weights['peso'], dicionario))

for i in range(0, len(dicionario)): # Estamos inserindo valores na nossa tabela
    cursor.execute("INSERT INTO clientes (nome, peso) VALUES (?, ?)", (nomes[i], pesos[i]))
conn.commit()  # e aqui estamos enviando para a nossa tabela os valores

# Atualizando o valor de alguma coisa
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome': 'José', 'id': 2})
conn.commit()

cursor.execute('SELECT * FROM clientes')  # e aqui nos buscamos os dados

for linha in cursor.fetchall():  # nos podemos usar isso como um iterador
    print(linha)
    identificador, nomes, pesos = linha
    print(identificador, nomes, pesos)
# É uma boa prática de programação fechar a conexão com o banco de dados
cursor.close()
conn.close()
