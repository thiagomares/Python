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
    if instrutor == False:
        print(f'{nome}')
    else:
        print('Rala peito')


mostra_info('Gustavo')
# Se queremos que um parâmetros seja modificado, basta que endereçamos ela  dentro do argumento
mostra_info(instrutor=True)

"""
    Por que utiliar parametros com valor defaut?

        - Nos permite ser mais flexiveis com nossas funçoes
        - Evita erros com parâmetros mais complexos complexos
        - Nos permite trabalhar com exemplos mais legiveis no código

    Quais tipos de dados que podemos utilizar como default de parâmetros?

        Todos, desde dados primitivos como ints e floats até Funções

    
"""
# Utilizando funções como parâmetros


def teste(teste=mostra_info(input('Digite Olá mundo \n'))):
    return teste


teste()

# Escopo = Evitando uns B.O. aí...
# Variáveis Locais
# Varíaveis globais

nome = 'Thiago'  # Esta é uma variável global


def diz_oi():
    print(f'Oi, {nome}')


diz_oi()

# Utilizando variável local


def diga_olá():
    nome = 'Thalia'
    print(f'Olá, {nome}')


diga_olá()
print(nome)

"""
    OBS: Se tiver uma variável local com o mesmo nome de uma variavel global, a variável local apenas modificará o que estiver dentro da função.

    Se puder evitar variaveis globais, evite.

    Em python, nos não podemos inicializar uma variável sem declarar-la anteriormente com um valor.
"""
