"""

    Mapas => Conhecidos em python como dicionários

    Dicionários em python são representados por chave {}

"""

receita = {'Jan': 300, 'Fev': 302, 'Mar': 650}

# Como iterar em dicionários

for chave in receita:
    print(receita[chave])


for chave in receita:
    print(f'{chave}: {receita[chave]}')

# Para termos acesso a todas as chaves, utilizamos do método keys da seguinte forma
# Eles serão impressos com o prefixo dict_keys

print(receita.keys())

# Para acessarmos os valores que estão presentes nas chaves, utilizamos o método values
# Tal Como nos keys, o values irá apresentar um prefixo dict_values

print(receita.values())

# Desempacotando valores

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Encontrando maximo, minimo, soma e o tamanho do dicionário

print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
print(sum(receita.values()))
