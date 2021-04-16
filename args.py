"""
    Entendendo o *args

    O *args é um parâmetro como qualquer outro. Isto significa que você poderá chamar de qualquer coisa, desde que começe com o asterisco (*)

    Por convenção, utilizamos o nome *args para defini-lo.

    Mas o que é o args?

    O parametro args utilizado em uma funçao, coloca os valores extras informados como entradas em uma tupla. Desde já, lembrar que tuplas são imutaveis.
"""

# Exemplo 01

def soma(num1, num2, num3):
    return num1 + num2 + num3

print(soma(1, 2, 3))


