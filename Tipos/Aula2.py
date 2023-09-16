# Duck Typing
"""
    Se anda como pato, nada como pato e voa como pato, logo, é um pato.
    
    Entendido isso, se o dado tiver uma estrutura muito semelhante ao de um container, como uma classe com , uma string, um dicionario ou uma lista, ele vai ter comportamentos similares, independentemente do seu tipo
"""


class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))

# Exemplo de duck typing - String, Lista e Dicionário
nome = "Thiago Mares"
lista = [12, 33, 27, 49]
dicionario = {'thiago': 28, 'vandinha': 27}

print(len(nome), len(lista), len(dicionario))
print(type(livro), type(nome), type(lista), type(dicionario))
