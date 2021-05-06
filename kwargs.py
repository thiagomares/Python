""" 
    Entendendo o **kwargs

    Poderiamos chamar este argumento de batata, mas como existe uma convenção, nos o chamamos de kwargs mesmo.

    Este é mais um parâmetro, mas diferente do args, que coloca os valores extras numa tupla, o kwargs exige que utilizemos parametros nomeados e transforma estes parametros extras em um dicionário. Ou seja, estamos dando uma chave e um valor para o kwargs

    Nas nossas Funções, nos podemos ter:

    - Argumentos obrigatorios
    - *args
    - argumentos default
    - **kwargs
"""

# Exemplo


def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')
    #  Ele vai transformar estes valores em um dicionário


colors = cores(thiago='Azul', gustavo='Amarelo', andre='roxo')
print(cores())

#  Nem os parametros args e o kwargs não são obrigatórios.


# Outro Exemplo

def cumprimento_especial(**kwargs):
    if 'thiago' in kwargs and kwargs['thiago'] is 'Azul':
        return (f"Olá, {kwargs['thiago']}")


print(cumprimento_especial(gustavo='Rosa', thiago='Azul', andre='roxo'))


# Desempacotando dicts
def nada(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


dicionário = {'nome': 'Thiago', 'sobrenome': 'Mares'}
print(nada(**dicionário))

#  obs: Os nomes da chave em um dicionário devem ser o mesmo dos parametros da função
