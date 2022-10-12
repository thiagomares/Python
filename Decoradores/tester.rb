# frozen_string_literal: true

# Criando os atributos
class Rental
  attr_accessor :status, :customer, :price

  def initialize(status, customer, price)
    @status = status
    @customer = customer
    @price = price
  end
end

# Utilizando os atributos na classe
class Apresentacao
  attr_reader :rental

  def initialize(rental)
    @rental = rental
  end

  def status
    "A locação está #{@rental.status}"
  end

  def valor
    @rental.customer
  end
end

locacao = Rental.new('Ativa', 'Thiago', 290)
locacao.customer = 'Marilany'
apresenta = Apresentacao.new(locacao)

puts locacao.customer
puts apresenta.status
