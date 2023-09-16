# Type Hinting
"""
    O que é type hinting?
    
    é como se nos estivessemos escrevendo as nossas variaveis como se fossem em uma linguagem de tipagem estática, porem, mantendo a dinamicidade da linguagem
"""
# Aqui declaramos explicitamente que declaramos nossa variável como do tipo int
x: int = 23
print(type(x))

# Porém, aqui nos mudamos dinamicamente o tipo da variável para string
x = "Olá, mundo"
try:
    print(type(x))
except Exception as e:
    pass

# Declarando uma função com definição da entrada e a definição de saida dela


def cumprimentar(nome: str) -> str:
    return nome


print(cumprimentar("Thiago"))
print(type(cumprimentar(42)))
