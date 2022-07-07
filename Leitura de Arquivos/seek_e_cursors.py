''' 
    Seek e cursores
    
    seek() é utilizado para movimentar o cursor pelo arquivo
'''

arquivo = open('./texto.txt')


print(arquivo.read())

# O Python nao atualiza o texto sozinho, depende de uma nova leitura para ser carregado.

''' Movimentando o cursor pelo arquivo utilizando o seek '''

arquivo.seek(0)
# Seek() é utlizada para movimentação do cursor pelo arquivo. Ele recebe um paramentro onde queremos colocar o cursor, que no caso é a posição 0

# Temos tambem o readline, que lê linha por linha
print(arquivo.readline().split(' '))

# O readlines lê varias linhas
print(arquivo.readlines())


# quando encerramos os trabalhos com o arquivo, devemos encerrar a conexão

arquivo.close()
