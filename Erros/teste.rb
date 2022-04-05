require 'sqlite3'

banco_de_dados = SQLite3::Database.open 'Teste.db'
banco_de_dados.execute 'CREATE TABLE IF NOT EXISTS clientes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        senha TEXT,
                        username TEXT)'

# banco_de_dados.execute 'INSERT INTO clientes (nome, senha, username) VALUES (?, ?, ?)', name, senha_digitado, username
puts '1- Para cadastro, 2 para login'
menu = gets.chomp.to_i

class Entrada
  def cadastro(nome, usuario, senha)
    banco_de_dados = SQLite3::Database.open 'Teste.db'
    banco_de_dados.execute 'INSERT INTO clientes (nome, username, senha) VALUES (?, ?, ?)', nome, usuario, senha
  end

  def entrada(usuario, senha)
    if usuario == username && senha == senha_digitado
      puts "Olá, #{nome}"
      puts id
    end
  end
end

if menu == 1
  puts 'Digite seu nome'
  name = gets.chomp
  puts 'digite seu usuário'
  username = gets.chomp
  puts 'Digite sua senha'
  password = gets.chomp
  cadastro = Entrada.new
  cadastro.cadastro(name, username, password)
elsif menu == 2
  puts 'Digite seu usuário'
  username = gets.chomp
  for valor in banco_de_dados.execute 'SELECT * FROM clientes
        WHERE username LIKE ?', username
    id, nome, senha, usuario = valor
  end
  if username == usuario
    puts 'digite sua senha'
    password = gets.chomp
    if password == senha
      puts "Bem-vindo, #{nome}"
    elsif password = !senha
      puts 'Senha invalida'
    end
  elsif username = !usuario
    puts 'Usuário não existe'
  end
end

banco_de_dados.close
