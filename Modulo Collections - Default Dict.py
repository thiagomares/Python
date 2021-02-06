"""
    Módulo Collections - Default Dict

    Ao criarmos um dicionário, nos informamos um valor default, podendo utilizar um lambda para isso.
    Este valor sera utilizado sempre quando não houver valor definido
    Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default atribuido.

    Footnotes: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e 
                     retornar valores.
"""

# Fazendo o import do Default Dict
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario["Nome"]  =  "Thiago Ferreira Mares"
print(dicionario["outro"])
print(dicionario) # Desta forma, a expressão lambda irá adicionar de forma espontânea uma chave logo em sequencia, e assumindo o valor inserido na lambda.
