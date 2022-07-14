''' 
    String IO
    
    Para ler ou escrever dados em arquivos em arquivos do sistema operacional o software precisa ter permissão:
    
    - Leitura
    - Escrita
    
    
    StringIO > Utilizado para ler e criar arquivos em memória
'''

# Fazendo o import
from io import StringIO

# String qualquer
mensagem = 'Qualquer string'

# Podemos criar qualquer arquivo em memória já com uma string inserida ou mesmo vazia para inserir o texto depois

arquivo = StringIO(mensagem)

# Agora, tendo o arquivo, podemos utilizar tudo que sabemos
print(arquivo.read())

