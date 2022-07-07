# Para ler o conteudo de um arquivo, utilizamos a funçao integrada open

''' 
    Sobre o Open:
    
    A forma mais simples de utilização, nos passamos apenas um param de entrada, que no caso é o nome do arquivo a ser lido. Esta função retorna um TextIOWrapper e então trabalhamos com ele
    
    
    # Por padrão, a função open abre o arquivo em modo leitura.
'''

arquivo = open("./texto.txt")

print(arquivo)


# Para ler o conteudo do arquivo, deve-se usar read

print(arquivo.read())

''' 
    O python utiliza um recurso chamado cursor para trabalhar em arquivos. Ele funciona como um cursor quando estamos escrevendo
    
    A Função Read lê TODO O CONTEÚDO DO ARQUIVO
'''