""" 
    Para fazer manipulação de arquivos no OS, precisamos fazer a importação da lib OS
"""

import os
import sys

# getcwd() -> Pega o diretório de trabalho corrente (retorna o caminho absoluto)
print(os.getcwd())

# Para mudar o diretório, usamos o chdir()
os.chdir("..")
print(os.getcwd())

# Podemos verificar se um diretório é absoluto ou relativo
print(os.path.isabs(f"G:\Meu Drive\Dev\Python\Leitura de Arquivos\novo.txt"))

# Imprime o tipo de OS (Posix = Unix, NT = Windows)
print(os.name)

# Podemos ter mais detalhes sobre o OS
print(sys.platform)

# Podemos listar os diretorios com listdir (retorna no formato de lista)
print(os.listdir())

# Podemos listar os diretorios com mais detalhes com scandir
arquivos = tuple(os.scandir())
print(arquivos)

# Quando abrimos a função scandir, devemos fechar, pois abrimos um arquivo
arquivos.close()
