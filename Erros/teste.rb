require 'sqlite3'

banco_de_dados = SQLite3::Database.open 'Teste.db'
banco_de_dados.execute 'CREATE TABLE IF NOT EXISTS clientes
                        (id INTEGER AUTO INCREMENT PRIMARY KEY,
                        nome TEXT,
                        senha TEXT,
                        username TEXT)'


# banco_de_dados.execute 'INSERT INTO clientes (nome, senha, username) VALUES (?, ?, ?)', name, senha_digitado, username

puts 'Digite seu usuário'
username = gets.chomp
puts 'Digite sua senha'
senha_digitado = gets.chomp

for valor in banco_de_dados.execute 'SELECT * FROM clientes
    WHERE username LIKE ?', username
id, nome, senha, usuario = valor
end

if usuario == username && senha == senha_digitado
  puts "Olá, #{nome}"
  puts id
end
# puts banco_de_dados.execute 'SELECT * FROM clientes'
banco_de_dados.close
