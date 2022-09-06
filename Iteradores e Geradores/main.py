"""
Iterators e Iteráveis

Iterator é um elemento de programação que pode ser iterável, um objeto que retorna um dado, sendo um elemento por vez
quando uma função next é chamada

Iterable é um objeto que retorna um iterador quando a função iter() for chamada
"""

nome = 'Thiago' # Isso aqui é um iteravel

iterable = iter(nome) #Isso é um iterador
try:
    print(next(iterable))
except:
    pass

print(type(iterable))

'''
Para entender de forma fácil iterável e iterador.

O primeiro item do for é o iterador, o segundo item é o iterável
'''

for letra in nome:
    pass
