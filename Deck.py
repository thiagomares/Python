"""
    Módulo collections - Deque

    Podemos dizer que o deque é uma lista de alta performance.
"""

# Importando a lib deque
from collections import deque

# Criando Deque
Deck = deque('Thiago')
print(Deck)

# Adicionando Elementos no deque
Deck.append(deque('Ferreira'))
print(Deck)

"""
    O Deque por definição fará um slice dos itens nele inseridos, exceto se você 
    enviar uma string via append, por exemplo, que daí ele irá se comportar como uma
    lista.

    Mas toda vez que iserirmos um deque, ele fará um slice, e como toda lista, ele aceita
    valores de todos os tipos
"""

# AppendLeft e popleft
"""
    O Append left fará adições de itens ao inicio da lista, 
    que diferente de uma lista comum que adiciona somente itens ao fim da lista.
"""

Deck.appendleft(5)
print(Deck)

"""
    Assim como o append, também temos o pop left, que remove o primeiro valor da lista
    e assim como o pop comum, retorna o valor removido da lista
"""