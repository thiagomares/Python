require 'sqlite3'

banco_de_dados = SQLite3::Database.open 'Teste.db'
banco_de_dados.execute "CREATE TABLE IF NOT EXISTS clientes (id INTEGER AUTO INCREMENT PRIMARY KEY, nome TEXT, telefone INTERGER)"
banco_de_dados.execute "INSERT INTO clientes (nome, telefone) VALUES (?, ?)", 'Thiago', 31989190738


for valor in banco_de_dados.execute "SELECT * FROM clientes"
    id, nome, telefone = valor
    puts id, nome, telefone
end

banco_de_dados.close if banco_de_dados