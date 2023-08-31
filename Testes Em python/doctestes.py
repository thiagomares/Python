'''
    Doctests
    
    Doctestes são testes que colocamos na docstring das funçoes ou métodos python
    
    Para rodar um teste do doctest:
    python -m doctes -v <nomedomodulo>.py
'''

def soma (a, b):
    """Soma os numeros a e b
    
    >>> soma(1, 2)
    3
    """
    return a + b

print(soma(2, 3))
