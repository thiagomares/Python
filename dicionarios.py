"""
    Dicionários

    OBS: Em algumas linguagens de programação, os dicionarios python sao conhecidos como mapas, porque dicionarios são coleções do tipo chave/valor

    Nas listas e nas tuplas, os valores ficam implicitos, já nos dicionarios, o valor ficam explicitos

    Dicionarios são representados por chaves {}, da seguinte forma:

    print(type({}))

    Chave e valor são separados por dois pontos, onde o primeiro valor é a chave e o segundo é o valor

    Tanto chave quanto valor podem ser de qualquer tipo anteriormente visto, como string, int ou float e podem ser misturados valores, tal como uma lista ou uma tupla

"""
# Forma 1 (mais comum de usar)

paises = {'BR': 'Brasil', 'US': 'Estados Unidos', 'UK': 'Reino Unido'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum de usar)

paises = dict(BR='Brasil', US='Estados Unidos', UY='Uruguai')
print(paises)

# Forma 1
# Para acessar o valor que está endereçado a aquele valor, basta fazer tal como nas listas, porém com o nome dado ao endereço da memoria

print(paises['BR'])

# Caso tentamos fazer um acesso utilizando uma chave inexistente, teremos o erro KeyError

# Forma 2 - Acessando via get 
# Esta é a forma mais recomendada de se acessar valores

print(paises.get('AR'))

# Quando utilizamos da forma acima, ao invés de aparecer o KeyError, vai aparecer none



# Podemos inserir qualquer tipo de dados no dicionario, incluindo listas, tuplas, dicionários como chaves de dicionários

InformacoesDaCasa = {
    30850-650: 'CEP da Casa',
    3135825881: 'Telefone da Casa'
}

print(InformacoesDaCasa)
print(type(InformacoesDaCasa))

# Tuplas são bastante interessantes de serem utilizadas  como chaves de dicionários, pois tuplas são imutáveis.

# Adicionar elementos em um dicionario
# Forma 1

pais = input("insira a sigla do pais e em seguida o nome do pais \n")
pais = pais.split(' ')
paises[pais[0]] = pais[1]

print(paises)

# Forma 2
NovoPais = {'ES': 'Espanha'}

paises.update(NovoPais)
print(paises)


# Atualizando dados
# Forma 1

paises['ES'] = 'Espanhol'
print(paises)

# Forma 2

paises.update({'ES': 'Espanha'})
print(paises)

"""
    Conclusão 1: A forma de atualizar dados ou inserir novos dados é a mesma

    Conclusão 2: Em Dicionários NÃO podemos ter chaves repetidas
"""

# Remover Dados de um dicionário
# Forma 1

paises.pop("AR") # Aqui precisamos sempre informar a chave, caso não encontre o elemento, retornará erro
print(paises)

# Obs 2: Ao removermos um objeto, o valor deste objeto é retornado

# Forma 2

del paises['US'] # Caso não se encontre o valor, será retornado erro
print(paises)

# Fazendo um carrinho de compras com dicionários

produto1 = {'Produto': 'PlayStation 4', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'Produto': 'Gran Turismo 4', 'Quantidade': 1, 'Preço': 230.00}


carrinho = {}
carrinho[1] = (produto1)
carrinho[2] = (produto2)


'''

    Da forma apresentada, é possível remover e adicionar produtos com facilidade ao carrinho, e
    além desta comodidade, também temos certeza das informaçoes que estão indexadas

'''

print(carrinho)


# Limpar o dicionario =  zerar dados

carrinho.clear()

print(carrinho)

# Para copiar um dicionário, utilizamos o comando copy *(deep copy)

carrinho = produto1.copy()
produto1['frete'] = 22.90
print (carrinho)


# Shallow Copy

carrinho = produto1

carrinho["frete"] = 22.90
print(carrinho)


# Podemos criar varias chaves de uma unica vez utilizando fromkeys

nome = {}.fromkeys(['Nome', 'Sobrenome', 'Nome do Meio'], )
print(nome)

