"""
# Dunder

dunder = double under

Os dunder são utilizados em funções e em outros objetos para que não exista confusão com outros itens

Em python, quando utilizamos módulos (import lib...) diretamente na linha de comando, internamente,
o python interpreta aquilo como uma variável __name__ e __main__ indicando que este módulo é o módulo
de execução principal.
"""

import teste
import classes

retorno = teste.Retorno('Marilany', 'Ferreira')
print(retorno.teste_original())
print(retorno.teste())
print(retorno.outro())


# Em suma, podemos deixar o __name__ = '__main__' como testes
# dentro do módulo para que não tenhamos problemas de importação ou algo do tipo
