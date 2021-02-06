"""
    Módulo Collections - Ordered Dictionaries
"""

# Importando o Ordered Dict
from collections import OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {"a": 1, "b": 2, "c": 3, "d": 4}

for chave, valor in dicionario.items(): 
    print(f'Chave = {chave}, Valor = {valor}') 

    """
        Lembrete rápido sobre a iterabilidade

        Quando temos dois valores no for, o primeiro valor é referente ao que seria a chave do slot e o segundo valor é referente ao valor que está conectado a chave

        por exemplo: Temos o valor "chave" para iterar com o valor da chave, e "Valor" para iterar com os valores desta chave, então, quando fazemos um for, estamos fazendo a 
        seguinte coisa:

            dicionario(chave) = valor

            Onde Chave internamente coleta o valor da chave que está naquela posiçao de memoria enquanto valor coleta o valor daquela chave.
    """

# Criando um ordered dict

dicionario = OrderedDict({"d": 4, "c": 3, "a": 5, "b": 2})
print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave = {chave}, Valor = {valor}') 