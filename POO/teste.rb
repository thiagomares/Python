# frozen_string_literal: false

# Classe principal do programa
class Produto
  # Iniciando os getters e setters

  attr_accessor :nome, :preco, :descricao, :imposto

  @imposto = 1.2
  @@contador = 0

  # Definindo nossos atributos

  def initialize(nome, preco, descricao)
    @nome = nome
    @preco = preco
    @descricao = descricao
    contador = @@contador + 1
    @@contador = contador
  end

  # Métodos

  def calcula_imposto
    @preco * @imposto
  end

  def contador
    @@contador
  end
end

p1 = Produto.new('PS5', 3500, 'Video Game')

# Criando atributos de instancia
p1.instance_eval do
  def acrescimo
    @acrescimo
  end

  def acrescimo=(valor)
    @acrescimo = valor
  end
end

p1.acrescimo = 300
p1.imposto = 1.42
puts p1.calcula_imposto + p1.acrescimo
puts p1.contador

p2 = Produto.new('PS5', 3500, 'Video Game')
puts "Ho\n" * 3
