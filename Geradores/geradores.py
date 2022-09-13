# Geradores
""" 

    Geradores são iteradores, mas nem todo iterador é um gerador

    Info:
    
        - geradores podem ser criados com funções geradores
        - funções geradoras utilizam a palavra reservada yield
        - geradores podem ser criados com expressões geradoras
"""

"""
    Funções utilizam return, geradores utilizam yield
    funções retornam uma vez, geradores retornam várias vezes
    funçao retorna um valor, geradores retorna um valor
"""

def conta(max):
    contador = 1
    while contador <= max:
        yield contador
        contador += 1
        

# Uma função geradora não é um generator, ela gera um generator.        '

iterador = iter(conta(15))
print(next(iterador))
