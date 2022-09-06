"""
Criando meu proprio loop
"""

for n in range(1,5): print(n)

# De forma oculta, o python faz da seguinte forma
iter(range(1, 5))

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for("Thiago Mares")
""" Explicando de forma fácil"""
"""
    Enquanto o while for verdadeiro (existir o que iterar) ele vai iterar, senão ele vai parar
    
    Ou seja, o for só é possivel com a existência da condição verdade do while.
"""
