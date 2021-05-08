''' 
    List Comprehensions

    - Utilizando list comprehensions, nos podemos gerar novas listas com dados processados a partir de outros iteraveis

    Sintaxe da list comprehension:

        [dado for dado in interavel]
'''

# Exemplo 1
numeros = []

for i in range(1, 11, 1):
    numeros.append(i)

print(numeros)

res = [numero * 10 for numero in numeros]
'''  
    Tecnicamente estamos fazendo algo parecido com um do, porem usando um for

    faça x enquanto iteramos sobre isso
'''

# List Comprehensions x Loop


# Loop
dobrados = []
for i in numeros:
    dobrado = i*2
    dobrados.append(dobrado)
print(dobrados)

# Fazendo a Mesma coisa em list comprehension
dobrados = [i*2 for i in numeros]
print(dobrados)

nome = 'Thiago'
print([letra.split() for letra in nome])

# Outro Exemplo 

nomes = ['thiago', 'gustavo', 'chislainy', 'marilany', 'josé']
print([letrados.capitalize() for letrados in nomes])
