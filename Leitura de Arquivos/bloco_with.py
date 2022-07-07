"""
    Bloco With

    O Bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados logo
    apos o logo with
"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
