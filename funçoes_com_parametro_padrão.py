"""
    Funções com parâmetro padrão

    Funçoes onde a passagem de parametro seja opcional.
"""
# Exemplo de função onde a passagem de parametro seja opcional
print('Thiago')

print()


def quadrado(numero):
    return numero ** 2


# Exemplo de função onde a passagem de parametro seja obrigatoria
print(quadrado(2))
# Aqui o compilador irá retornar um Type Error caso não dermos um argumento para o parametro
print(quadrado(0))


def pow(valor, potential=2):  # Desta forma, nos não precisamos endereçar um valor obrigatoriamente ao segundo parâmetro, caso não retornemos o valor para o parametro, ele ira considerar que ele tem um valor de 2
    return valor ** potential


print(pow(3))

# Exemplo mais complexo


def mostra_info(nome='Thiago', instrutor=False):
    if nome == 'Thiago' and instrutor == False:
        print('Thiago')
    else:
        print('Rala peito')


mostra_info('Gustavo')
