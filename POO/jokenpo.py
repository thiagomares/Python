import random

class Machine:
    
    def __init__(self, valor):
        self.__valor = valor
        self.__selecao = None

    def maquina(self):
        self.__selecao = random.choice(['pedra', 'papel', 'tesoura'])
        return self.__selecao

    def escolha(self):
        if self.__valor == 'papel':
            if self.__selecao == 'papel':
                return 'empate'
            elif self.__selecao == 'pedra':
                return 'Venceu'
            elif self.__selecao == 'tesoura':
                return 'perdeu'
        elif self.__valor == "tesoura":
            if self.__selecao == 'papel':
                return 'venceu'
            elif self.__selecao == 'pedra':
                return 'perdeu'
            elif self.__selecao == 'tesoura':
                return 'empate'
        elif self.__valor == 'pedra':
            if self.__selecao == 'papel':
                return 'perdeu'
            elif self.__selecao == 'pedra':
                return 'empate'
            elif self.__selecao == 'tesoura':
                return 'tesoura'


usuario = input('Escolha entre pedra, papel ou tesoura \n').lower()
maquina = Machine(usuario)
print(f'A maquina escolheu {maquina.maquina()}')
print(f'Você {maquina.escolha()}')
