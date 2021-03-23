"""
    Documentando funçoes com docstrings


    Uma docstring é um comentário com aspas duplas triplicadas
"""


def diga_oi():
    """ Uma função que diz oi """
    return 'Oi'

# Imprimindo o que está na função
print(diga_oi())

# Fazendo a consulta da documentação a partir do metodo doc
print(diga_oi.__doc__)

# Podemos ainda fazer acesso a documentação a partir da função help
print(help(diga_oi))
