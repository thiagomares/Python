'''
    Fazer um programa que leia se um numero inteiro é impar ou par
'''

contador = 0

while(contador <= 100):

    verificador = input('Verificando \n')
    
    if verificador.isdigit():

        verificador = int(verificador)

        if verificador % 2 == 0 and verificador != 0:
            print('Este número é par')
        elif verificador % 2 != 2 and verificador != 0:
            print('Este número é impar')
        else:
            print('Este número é zero')

        parar = input('Deseja Parar? ')

        if parar == 'Y' or parar == 'y':
            break

    else:
        print('Não é um valor válido')
