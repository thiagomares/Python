# -*- coding: utf-8 -*-

""" 
    assertions - afirmações
    
    
    em python, utilizamos a palavra reservada assert para realizar
"""

#Teste

def Soma(a, b):
    assert a > 0 and b > 0, 'Numeros precisam ser positivos'
    return a + b

print(Soma(2, 3))
