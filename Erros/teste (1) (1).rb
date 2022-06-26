require 'sqlite3'

banco_de_dados = SQLite3::Database.open 'Teste.db'
banco_de_dados.execute 'CREATE TABLE IF NOT EXISTS clientes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        senha TEXT,
                        username TEXT)'

puts '1- Para cadastro, 2 para login'
menu = gets.chomp.to_i

class BancoDeDados
  attr_accessor :nome, :usuario, :senha

  def cadastro
    banco_de_dados = SQLite3::Database.open 'Teste.db'
    banco_de_dados.execute 'INSERT INTO clientes (nome, username, senha) VALUES (?, ?, ?)', nome, usuario, senha
  end

  def entrada
    banco_de_dados = SQLite3::Database.open 'Teste.db'
    for valor in banco_de_dados.execute 'SELECT nome, username, senha FROM clientes WHERE username LIKE ?', usuario
      nome, username, password = valor
    end
    puts "Olá, #{nome}" if usuario == username && password == senha
  end
end

bancodedados = BancoDeDados.new

if menu == 1
  puts 'Digite seu nome'
  bancodedados.nome = gets.chomp
  puts 'digite seu usuário'
  bancodedados.usuario = gets.chomp
  puts 'Digite sua senha'
  bancodedados.senha = gets.chomp
  bancodedados.cadastro
elsif menu == 2
  puts 'Digite seu usuário'
  bancodedados.usuario = gets.chomp
  puts 'Digite sua senha'
  bancodedados.senha = gets.chomp
  bancodedados.entrada
end


banco_de_dados.close
