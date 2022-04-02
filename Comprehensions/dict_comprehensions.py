""" 
    Dict comprehensions

    Se quisermos criar uma lista, fazemos da seguinte forma

    lista = [1, 2, 3, 4]

    Uma Tupla:

    tupla = (1, 2, 3, 4)

    Um Conjunto

    set = {1, 2, 3, 4}

    Mas, para criar um dicionário...precisamos inserir chave e valor

    dicionário = {1: 'um', 2: 'dois', 3: 'três'}
"""

# Sintaxe do dict comprehension

dictionary = {1: 'um', 2: 'dois', 3: 'três'}

# Para que possa funcionar, deve-se utilizar o método Items
dicionario = {i: chave for i, chave in dictionary.items()}
print(dicionario.items())

# Utilizando de listas para iterar sobre dicts

lista = [1, 2, 3, 4]
outro_dicionario = {valor: valor for valor in lista}
print(outro_dicionario)

# Misturando string e algum iterável

chaves = 'Thiago'
lista = [1, 2, 3, 4, 5, 6]

mistura = {chaves[i]: lista[i] for i in range(0, len(chaves))}
print(mistura)
