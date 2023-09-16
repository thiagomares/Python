# dados dinamicos x dados estaticos

""" 
    No python, nos temos os dados sendo criados de forma dinamica, ou seja, o tipo desses dados podem mudar da forma que for mais conveniente
"""

valor1 = 15
valor1 = "Vandinha"

# Acima nos criamos uma variavel do tipo inteiro, e depois assimilamos esta variável para o tipo string, e nos dois casos inserimos esses dados de forma implicita, ou seja, o proprio codigo interpreta a mudança deste valor e a assimilação para a nova classe

print(type(valor1)) # E aqui visualizamos esta tipagem

# Da mesma forma, podemos declarar a variavel de forma que ela assimila, dando a ela o tipo de dado que ela deve receber, e diferentemente do javascript, ele nao vai forçar uma mudança de tipo, quando concatenamos dois tipos de dados distintos

valor2 = str("Olá, Mundo")
valor2 = 15
print(type(valor2))


# Já nas linguagens que usam tipagem forte, você ja deve declarar o tipo de dado na declaração da variavel, como podemos ver no arquivo TiposJava.Java

