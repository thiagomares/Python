'''
    Verifica o tamanho de um nome e fala o tamanho do nome
'''

nome = input('Digite seu nome \n')

if len(nome) <= 4:
    print('Seu Nome é curto')
elif len(nome) > 5 and len(nome) <= 6:
    print('Seu Nome é normal')
elif len(nome) > 6:
    print('Seu nome é longo')