'''
    Programa que verifica a hora e dá uma saudação
'''

verifica_hora = int(input('Digite a hora \n'))

if verifica_hora > 0 and verifica_hora < 11:
    print('Bom Dia')
elif verifica_hora > 12 and verifica_hora < 18:
    print('Boa Tarde')
elif verifica_hora > 18 and verifica_hora < 23:
    print('Boa noite')
else:
    print('Hora inválida')
