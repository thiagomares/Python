"""
    Escrevendo em arquivos

    Quando abrimos um arquivo em modo leitura, somente podemos realizar leitura nele,
    e no modo escrita é da mesma forma
"""

with open('novo.txt', 'w') as arquivo:
    arquivo.write("Thiago Ferreira Mares")

with open('novo.txt') as arquivo:
    print(arquivo.read())


# Quando abrirmos um arquivo em modo escrita e ele não existe no nosso mundinho, o python vai tratar de criar
# um novo arquivo :)
