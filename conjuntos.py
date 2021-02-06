"""
    Conjuntos

    Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos da matemática

    Em python, os conjuntos são chamados de sets, dito isso, da mesma forma que na matemática:
        - Conjuntos não possuem valores duplicados.
        - Conjuntos não tem valores ordenados.
        - Elementos não são acessados via índices, ou seja, não são indexados.

    Conjuntos são aconselhaveis para se utilizar quando precisamos armazenar elementos, mas não nos importamos
    com a ordenação deles. Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

    Os sets são referenciados em python com {}

    Diferença entre conjuntos e mapas:

        - Um dicionário tem chave/valor
        - Um conjunto tem somente valor

"""

# Definindo um conjunto
# Forma 1

from typing import Sequence, Union


s = set({1, 3, 4, 5, 5, 2, 3, 7, 0}) # Ele não ira receber valores repetidos & irá os ordenar automaticamente
print(s)

# Forma 2

p = {10,20, 30, 40, 40, 41, 50, 12, 33, 21, 20}
print (p)
print(type(p))

# É possivel verificar se existe o valor dentro do conjunto, todavia, não é possível verificar se tem algo no slot da memória
# uma vez que essa memória não é endereçável.

if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# OBS: Diferentemente dos conjuntos que não recebem valores duplicados, os dicionários não recebem chaves duplicadas
# como assim? Caso haja duas chaves "A" com valores diferentes uma da outra, somente a segunda será aceita, pois é uma
# sobreposição a uma chave anteriormente adicionada.

# Assim como todo outra coleção python, podemos misturar todo tipo de dado em python

s = {"a", 12, 31, ("Vasco", "Botafogo", "SerieB")} 
print(s)

# Não podemos inserir uma lista em python.

"""
    Uso aplicado de conjuntos

    Imaginemos que tenha uma feira em que se coleta alguns dados dos visitantes, e quisessemos
    aferir o numero de pessoas de cidades distintas. Com a propriedade dos conjuntos em não receber
    valores duplicados, podemos assim listar a quantidade de cidades representadas na feira.

"""

ListaCidades = ["Belo Horizonte", "São Paulo", "Curitiba", "Santos", "São Paulo", "Nova York", "Belo Horizonte", "Boston", "St. Louis", "Santos"]
print(ListaCidades)
print(len(ListaCidades))

CidadesRepresentadas = set(ListaCidades)
print(CidadesRepresentadas)
print(len(CidadesRepresentadas))

# Adicionando elementos em um Conjunto 
# Para adicionar elemento ao set, basta usar o comando add

s.add(4)
print(s)

# Para Remover elementos do conjunto, basta utilizar o comando remove
# Forma 1
s.remove(4)
print(s)

# obs: Caso o valor informado para sua remoção não exista dentro do conjunto, o código retornará erro

# Forma 2 - Utilizando o Discard
s.discard(2)
print(s)

# Diferentemente do remove, caso o valor que quiséssemos excluir não estiver no conjunto, o codigo não apresentará erros

# Copiando um conjunto para outro
# Forma 1 - Deep copy

Conjunto = s.copy()
print(Conjunto)

Conjunto.add(4)

print(Conjunto)
print(s)

# Forma 2 - Shallow copy

Conjunto = s # Se a = b, todo valor que A recebe, B também recebe. Se todo valor de A é removido, todo valor de B tbm é removido.
print(Conjunto)

Conjunto.add(4)
print(Conjunto)
print(s)

# Podemos remover todos os itens de um conjunto utilizando clear

s.clear()
print(s) # Quando limpamos todos os dados de um conjunto, no output ele mostrará set(), indicando que é um conjunto vazio.

# Métodos matemáticos de conjuntos

# Metodo de união
# Forma 1

ConjuntoA = set(range(1, 10))
ConjuntoB = set(range(5, 20))
print(ConjuntoA)
print(ConjuntoB)

ConjuntoResultante  = ConjuntoA.union(ConjuntoB)
print(ConjuntoResultante)


# Forma 2 -  Utilizando pipe

ConjuntoResultante = ConjuntoA | ConjuntoB
print(ConjuntoResultante)

# Gerar um conjunto em ambos os conjuntos tem valores iguais
# Forma 1 - Criando com Intersection

ConjuntoResultante = ConjuntoA.intersection(ConjuntoB)
print(ConjuntoResultante)

# Forma 2 - Utilizando &
ConjuntoResultante = ConjuntoA & ConjuntoB
print(ConjuntoResultante)

# Gerar um conjunto de valores em dois conjuntos não compartilham o mesmo valor
# Forma 1 - utilizando difference

ConjuntoResultante = ConjuntoA.difference(ConjuntoB)
print(ConjuntoResultante)

# Soma, Maximo, Minimo e comprimento de conjuntos

print(sum(ConjuntoA)) # Soma
print(min(ConjuntoA)) # Valor Minimo
print(max(ConjuntoA)) # Valor maximo
print(len(ConjuntoA)) # Comprimento do conjunto
