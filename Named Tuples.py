"""
    Named Tuples

    Uma tupla nomeadas são tuplas diferenciadas, onde especificamos um nome e parâmetros para a tupla
"""
# Importando a biblioteca named tuples

from collections import namedtuple

# Precisamos definir o nome e parâmetros
# Forma 1 - Declaração named tuple

cachorro = namedtuple('Cachorro', 'Idade Raça Nome')

# Forma 2 - Declaração named tuple

cachorro = namedtuple('Cachorro', 'Idade, Raça, Nome')

# Forma 3 - Utilizando named tuple e lista

cachorro = namedtuple('Cachorro',['Idade', 'Raça', 'Nome'])

# Passando valores para a named tuple

Leo = cachorro(Idade=10, Raça='Fox Paulistinha', Nome='Leo')

print(Leo)

# Acessando os dados
# Forma 1
print(Leo[0])

# Forma 2
print(Leo.Idade, Leo.Raça, Leo.Nome)

# Desta forma, podemos acessar exatamente o que queremos, a forma 1 somente nos permite acessar via index


