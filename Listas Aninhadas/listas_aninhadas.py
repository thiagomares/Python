""" 
    Listas aninhadas (nested lists)

    Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays, arrays estes que podem ser unidimensionais(vetores), ou multidimenisonais (matrizes), como em C#, Java, PHP...

    Em python não existe array uni ou multidimensionais, existe apenas listas
"""

# Exemplo 1

# Exemplo de listas aninhadas
lista1 = [1, 2, 3, 4, 5, 6, [1, 3, 5], [2, 4, 6]]

print(lista1, type(lista1))

# Como fazemos para acessar os dados
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# aqui estamos tentando acessar o numero 3 da primeira lista
print(lista2[0][2])

for lista in lista2:
    for numero in lista:
        print(numero)

# Fazendo list comprehensions com listas aninhadas
[[print(valor) for valor in listas] for listas in lista2]

# Criando um vetor 3x3

tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]

print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['x' if num % 2 == 0 else 'o' for num in range(
    1, 4)] for valor in range(1, 4)]

print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)]for j in range(1, 4)])
