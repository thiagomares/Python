# Manipulação de arquivos

import os
import sys
from send2trash import send2trash as lixeira
from venv import create

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('pandas.ipynb'))

# Criando arquivos
open('novoarquivo.txt', 'w').close()

# Criando arquivos
try:
    # Só funciona no unix (Mac depende de SUDO)
    os.mknod('../iteradores/iteradores.py')
except:
    pass


# Criando diretorios
try:
    # O exist_ok faz com que o python ignore caso exista um diretorio com o mesmo nome
    os.mkdir('../Iteradores', exist_ok=True)
    with create('../Iteradores/iteradores.py') as iteradores:
        pass
except:
    pass

# Renomeando Diretorios (se o diretorio nao estiver vazio, vai subir um OSerror)
try:
    os.rename('./.idea', 'Idea')
except:
    pass
finally:
    os.rename('./Idea', '.idea')


# Quando queremos excluir um arquivo(remove) ou uma pasta(removedir) mas não eliminar completamente da maquina, devemos utilizar a lib send2trash

try:
    lixeira('novoarquivo.txt')
except:
    pass


""" 
    Quando formos utilizar de pastas temporárias, podemos utilizar a lib tempfile.TemporaryDirectory()
    
    Utiliza-se um input() apenas para manter os arquivos disponiveis
"""