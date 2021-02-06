"""
    Modulo Collections - Counters

    Collections => Hi-Performance Container Datatypes (Tipos de dados de container de alta performance)

    Todas as coleçoes vistas em coleções são um tipo de container, uma vez que estes dados conseguem
    armazenar todo e qualquer tipo de dado, claro, que com sua determinada regra de uso.

    Counter -> Recebe um iteravel (String, lista, tupla, dicionario e por ai vai) como parametro e 
    cria um objeto do tipo collections - counter que é semelhante
    a um dicionário, contendo como chave o elemento da lista passada como parametro e como valor  a quantidade de 
    ocorrencias deste elemento.

"""

# Utilizando o counter

from collections import Counter # E desta forma nos conseguimos importar uma biblioteca, no caso o Counter da biblioteca Collections

Lista = list(range(1, 11))
Lista.append(33)
Lista.append(3)
Lista.append(3)
Lista.append(4)
Lista.append(5)
print(Lista)

# Utilizando o Counter
res = Counter(Lista)

"""

    O counter funciona como uma especie de contador de valores que estão adicionados a lista

    Por exemplo, se temos o numero x aparecendo na lista 3 vezes, um outro valor Y aparecendo 6 vezes
    ele irá ordenar estes valores pelo numero de recorrencias que eles tiverem nesta lista/tupla/dicionario/conjunto

    E como ele exibe estes valores:

        Counter({X: Y}), onde:

        X é o valor que está sendo quantificado
        Y é a quantidade de ocorrências do valor quantificado
    
"""

print(type(res))
print(res)
print(Counter(Lista))

# Fazendo Counter de uma string

print(Counter("Thiago Ferreira Mares"))


# Texto longos

texto = """At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis
 praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati
  cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.
   Et harum quidem rerum facilis est et expedita distinctio.
 Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat
  facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. 
  Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates 
  repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, 
ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat"""

# Desta forma, conseguimos separar palavra por palavra de uma string, e contar quais palavras se repetem na string como um todo
palavras = texto.split(" ")
print(Counter(palavras))

resultado = Counter(palavras)
print(resultado.most_common(5)) # Com este método, podemos exibir quais são os valores mais comuns na string