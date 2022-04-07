require 'sqlite3'

db = SQLite3::Database.open 'Teste.db'


class Acoes
    attr_accessor :nome, :sobrenome
    
    def inserir
        puts nome, sobrenome
    end
end

acoes = Acoes.new
acoes.nome = gets.chomp
acoes.sobrenome = gets.chomp

acoes.inserir