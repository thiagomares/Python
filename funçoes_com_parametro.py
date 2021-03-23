'''
    Funções com parametro 

    - Quando dizemos funçoes com parametro, falamos de funções que tem recebem dados para serem processados da função

    Se pensarmos em funções, nos podemos ter funções que:

        - Não possuem entradas
        - Não possuem saidas
        - Possuem entrada mas não possui saidas
        - Não possui entrada, mas possui saidas
        - possui entrada e saidas
'''

# Exemplo de função com parametro


def Função(Parametro):
    print(Parametro)


Função('Thiago')


class classe():  # Exemplo de classe no Python
    def outra_funcao(argumentos):
        print(argumentos)


classe.outra_funcao('Thalia')

# Refatorando uma funçao


def Quadrado():
    return 7*7


print(Quadrado())

valor_user = input(
    'Digite o valor que deseja descobrir seu valor ao quadrado \n')
valor_user = float(valor_user)
print(valor_user)
print(type(valor_user))

# Função que soma dois valores
def Pow(valor1, valor2):
    return valor1 + valor2


print(Pow(input('Digite os dois valores que deseja calcular \n'),
      input('digite o valores que deseja calcular \n')))


# Quando utilizamos funções com parametro, nos devemos enviar o mesmo numero de argumentos que o numero de funções tem. Exemplo: Se temos dois parametros na função, devemos dar dois argumentos para que aquela função seja satisfeita
