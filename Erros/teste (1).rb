require 'byebug'
require 'sqlite3'
require 'faker'
require 'cpf_utils'

class Cadastro
  def initialize
    @connector = SQLite3::Database.new 'teste.db'
    @cadastro = []
  end

  attr_accessor :cpf, :nome, :cep

  def coleta_dados
    for i in @connector.execute 'SELECT * FROM teste'
      @cadastro.append({ "nome": i[1], "endereço": i[2], "email": i[3], "CPF": i[4], "CEP": i[5] })
    end
  end

  def cria_tabela
    @connector.execute 'CREATE TABLE IF NOT EXISTS teste
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    endereço TEXT,
                    email TEXT,
                    cpf INTEGER,
                    cep INTEGER)'
  end

  def inserir
    nome = Faker::Name.name
    endereco = Faker::Address.street_address
    email = Faker::Internet.email
    cpf = CpfUtils.cpf
    cep = Faker::Address.zip

    connector = SQLite3::Database.new 'teste.db'
    connector.execute 'INSERT INTO teste (nome, endereço, email, cpf, cep) VALUES (?, ?, ?, ?, ?)', nome, endereco, email, cpf, cep
  end

  def retorna_cadastros
    @cadastro
  end

  def busca_cadastro_cpf
    for i in @cadastro
      user = i if i[:CPF] == self.cpf
    end
    if user.nil?
      puts 'Usuário não encontrado'
    else
      puts "Bem-vindo, #{user[:nome]}"
    end
  end
  def busca_cadastro_nome
    for i in @cadastro
      user = i if i[:nome] == self.nome
    end
    if user.nil?
      puts 'Usuário não encontrado'
    else
      puts "O endereço do usuário é #{user[:endereço]}"
    end
  end

  def busca_cadastro_endereco
    user = []
    for i in @cadastro
      user.append(i[:nome]) if i[:CEP] == self.cep
    end
    if user == []
      puts 'Usuário não encontrado'
    else
      puts "Usuários neste CEP são:"
      for i in user
        puts "#{i}"
      end
    end
  end
end

cadastro = Cadastro.new
cadastro.cria_tabela
cadastro.coleta_dados
cadastro.inserir
puts cadastro.retorna_cadastros
cadastro.cep = 30302
cadastro.busca_cadastro_endereco

