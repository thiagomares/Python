"""
    Entendendo o *args

    O *args é um parâmetro como qualquer outro. Isto significa que você poderá chamar de qualquer coisa, desde que começe com o asterisco (*)

    Por convenção, utilizamos o nome *args para defini-lo.

    Mas o que é o args?

    O parametro args utilizado em uma funçao, coloca os valores extras informados como entradas em uma tupla. Desde já, lembrar que tuplas são imutaveis.

    Exemplo: queremos fazer uma soma de 3 valores, so que é fornecido um quarto valor e em condições normais este codigo irá retornar erro pois ele vai ter mais argumentos que ele poderia receber, contudo, se utilizarmos o *args, ele como se comporta como uma tupla, não tem problema receber varios e varios valores.
"""
import pygame
# Exemplo


def soma(*args):
    return args[0] + args[1] + args[2], args[3]
    # Neste exemplo de cima, estou coletando os tres primeiros valores do args e somando e por fim coletando o quarto valor e exibindo para o usuário qual é este valor


print(soma(1, 2, 3, 4))


# Podemos utilizar outro nome para o *Args

def outra_soma(*argumentos):
    lista = []
    lista = argumentos
    return argumentos[0] + argumentos[1] + argumentos[2], argumentos[3], lista, sum(argumentos)


print(outra_soma(-1, -4, 20, 15))

# Quando damos o argumento * ao python, ele interpreta que é para desempacotar aqueles valores dados
num = [1, 2, 3, 4, 5, 6]
print(outra_soma(*num))
