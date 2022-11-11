import random


def maquina():
    selecao = random.choice(['pedra', 'papel', 'tesoura'])
    return selecao

maquina = maquina()
usuario = input('Escolha entre pedra, papel ou tesoura \n').lower()
print(f'A maquina escolheu {maquina}')

if usuario == 'papel':
    if maquina == 'papel':
        print('empate')
    elif maquina == 'pedra':
        print('Venceu')
    elif maquina == 'tesoura':
        print('perdeu')
elif usuario == "tesoura":
    if maquina == 'papel':
        print('venceu')
    elif maquina == 'pedra':
        print('perdeu')
    elif maquina == 'tesoura':
        print('empate')
elif usuario == 'pedra':
    if maquina == 'papel':
        print('perdeu')
    elif maquina == 'pedra':
        print('empate')
    elif maquina == 'tesoura':
        print('tesoura')


