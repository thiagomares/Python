"""
    Tuplas (tuples)

    Tuplas são extremamente parecidas com listas. 
    
    Existe praticamente duas diferenças com as listas:

        - As tuplas são representadas por parentesis.

        - As tuplas são imutáveis. Isso significa que ao se criar uma tupla, ela não se modifica, 
        tendo um comportamento semelhante ao de uma constante. Toda operação em uma tupla faz com
        que gere uma nova tupla.

    OBS:
        - As tuplas são representadas por parentesis, porém, como o python tem uma tipagem de certa forma
        dinâmica, ele consegue entender que, quando declaramos uma variável com múltiplos valores separados
        por vírgula, ele transforma os valores em uma tupla.

        - Tuplas com um elemento, devido a natureza do python em ser uma linguagem dinâmica, fará com que
        a tupla se torne uma variável, seja ele integer, float, ou string. Ele sempre irá assumir que aquele
        valor é uma variável e não mais uma tupla, mesmo declarando-a com parentesis, como é dito em seus
        repositórios. Para se declarar uma tupla com um elemento, devemos declara-la com uma vírgula logo
        em seguida ao valor declarado.


    Dito isso, podemos concluir que:
        Tuplas são declaradas a partir de valores endereçados a uma variável, separados por vírgula
        e podem ou não serem declaradas com parentesis para que, desta forma, seja diferenciado de uma
        lista comum.

    
"""

# Exemplo de uma tupla comum, com strings

tuplaString = ("ola mundo", "Vai Cair, cruzeiro")
print(type(tuplaString))
print(tuplaString)

# Gerando tuplas com range

TuplaAlcance = tuple(range(0, 11, 1))
print(TuplaAlcance)

"""
    Podemos gerar uma tupla automaticamente utilizando Range, pois o range primeiro fará com que seja calculado os valores para depois 
    atribuir estes valores gerados à variável de forma dinâmica.
"""

# Desempacotamento de Tuplas

tupla = "Thiago", "Ferreira", "Mares"

nome, nomedomeio, sobrenome = tupla
print(nome)
print(nomedomeio)
print (sobrenome)

"""
    Dado a natureza da tupla de ser imutável, diferentemente das listas, não há qualquer modo de adição ou remoção
    de valores inseridos na tupla. A tupla somente assume valores quando os endereçamos diretamente a ela.

    Entretanto, os métodos soma*, maximo, mínimo e tamanho são possíveis de serem utilizados com facilidade, porém, 
    o método soma só é possível se todos os valores da tupla sejam inteiros e/ou reais. Caso tenha um valor do tipo
    string, este jamais pode ser somado.
"""

tupla =  tuple(range(1, 10, 1))
print(sum(tupla))
print(len(tupla))

# Concatenação de Tuplas

tupla1 = 1, 2, 3, 4, 5
tupla2 = 6, 7, 8, 9, 10

print(tupla1 + tupla2) 

tupla1 = tupla1+tupla2 # Tuplas são imutáveis, porém, pode-se sobrescrever os valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla4 =  1, 2, 3, [1, 3, 5]
print(1 in tupla4)

# Iterando sobre as Tuplas

tupla4 =  1, 2, 3

for n in tupla4:
    print(n)

# Contando elementos em uma tuplas

tupla4 =  1, 2, 3, 3, 3, 2, 4, 1, 1

print(tupla4.count(3))

if tupla4.count(3) > 2:
    print(sum(tupla4))

# Dicas para Utilização de Tuplas


# Devemos utilizar tuplas sempre quando não precisarmos de modificarmos os valores contidos em uma coleção
# Exemplo

meses = "janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"

meses =  list(meses) # É possível converter tuplas para listas e vice e versa, utilizando uma linha de codigo como esta.

meses.append("October")

meses = tuple(meses)

print(meses)

# O acesso aos valores de uma tupla é semelhante ao de uma lista qualquer 

print(meses[4])

# Iterar via while
i = 0

meses = list(meses)

while i < len(meses):
    print(meses[i])
    if meses[i] == "October":
        meses[i] = "Outubro"
        print(meses[i])
    i = i + 1

# Slicing 
# Regra de slicings -> tupla[inicio:fim:passo]

print(meses[1::2])


"""
    Por quê utilizar tuplas?

        - Tuplas são mais rápidas que listas
        - Tuplas deixam seu código mais seguro, isto porque, trabalhar com elementos imutáveis traz mais segurança ao código
"""

# - Copiar uma tupla para outra

nova = meses # Na tupla, não temos o problema de shallow copy

print(nova)

