require 'sqlite3'

class Cadastro

    attr_accessor :endereco
    def initialize
      @connector = SQLite3::Database.new 'teste.db'
      @cadastro = @connector.execute 'SELECT nome FROM teste WHERE endereço LIKE ?', "%O'Conner%"
  
    #   for i in @connector.execute 'SELECT * FROM teste WHERE endereço LIKE ?', "%#{self.endereco}%"
    #     @cadastro.append({ "nome": i[1], "endereço": i[2], "email": i[3], "CPF": i[4] })
    #   end
    end

    def retorna
        @cadastro
    end
end

teste = Cadastro.new
teste.endereco = "Janae"
puts teste.retorna