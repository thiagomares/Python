# Gerenciamento de memória em python
#Python Global interpreter lock
"""
    É um mutex que permite apenas uma thread tome conta do intepretador python;

    O Impacto do gil nao é comumente visivel para devs que executem programas single-thread, mas pode ser uma dor de cabeça para programas que precisam de tempo de resposta em codigos
    multithread.

    desde que o gil permite apenas uma thread a ser executada, mesmo em computadores com arquitetura que permite utilizar mais de um core, o GIL tem ganho reputação de
    indecente do Python
"""

# mostrando o numero de referencias ao objeto a utilizando a lib sys e o metodo getrefcount
import sys

a =[]
b= a
print(sys.getrefcount(a))

""" 
    O deadlock é quando um lock deixa de existir e o lock está nele, e nisso travamos nosso programa
"""