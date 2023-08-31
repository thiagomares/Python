'''
    Doctests
    
    Doctestes são testes que colocamos na docstring das funçoes ou métodos python
    
    Para rodar um teste do doctest:
    python -m doctes -v <nomedomodulo>.py
    
    Saida do teste:
        5
    Trying:
        soma(1, 2)
    Expecting:
        3
    ok
    1 items had no tests:
        doctestes
    1 items passed all tests:
    1 tests in doctestes.soma
    1 tests in 2 items.
    1 passed and 0 failed.
    Test passed.
'''

def soma (a, b):
    """Soma os numeros a e b
    
    >>> soma(1, 2)
    3
    """
    return a + b

print(soma(2, 3))

# Outro exemplo, aplicando o TDD
def duplicar (valores):
    """
    Duplica os valores em uma lista 
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    
    >>> duplicar([])
    []
    
    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    
    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

