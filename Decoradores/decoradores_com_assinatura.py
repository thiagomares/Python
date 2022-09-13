# Decoradores com diferentes assinatura

# Relembrando

def gritar(funcao):
    def aumentar(*argumentos, **sobreargumentos):
        # Neste ponto, nos estamos aplicando upper em tudo que ele receber
        return funcao(*argumentos, **sobreargumentos).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'olá, eu sou {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, gostaria de {principal}, acompanhado de {acompanhamento}'


# Testando

print(saudacao('Thiago'))
print(ordenar('strogonoff', 'salada'))


# Aqui nos utilizaremos decorator pattern (que é um padrão de projeto)
# A forma de resolução disso é utilizando args e kwargs


print(ordenar(principal= 'Salada', acompanhamento= 'Batata'))

# Decoradores com parametros
def verifica(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                yield 'Incorreto'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica('Strogonoff')
def comidafavorita(*args):
    print(args)
