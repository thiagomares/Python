require 'sqlite3'

banco_de_dados = SQLite3::Database.open 'Teste.db'
banco_de_dados.execute "CREATE TABLE IF NOT EXISTS clientes (id INTEGER AUTO INCREMENT PRIMARY KEY, nome TEXT, telefone INTERGER)"
name = 'Thiago'
senha_digitado = 31989190738
# banco_de_dados.execute "INSERT INTO clientes (nome, telefone) VALUES (?, ?)", name, senha_digitado

dados = []
for valor in banco_de_dados.execute "SELECT * FROM clientes WHERE nome LIKE ?", name
    id, nome, telefone = valor
    dicionario = {'Nome' => nome, 'Senha' => telefone, 'codigo' => id}
    dados.push(dicionario)
end
for i in dados
    puts dados[i]
end
if nome == name
    if telefone == senha_digitado
        puts "Olá, #{name}"
        puts id
    end
end

banco_de_dados.close if banco_de_dados