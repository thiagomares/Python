"""
    Propriedades - Properties

    Basicamente nos estamos criando propriedades para nossos atributos. E para isso, utilizamos o decorador @property
"""

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

    # Criando nosso getter de nome
    @property
    def nome(self):
        return self.__nome

    # Criando nosso setter. Para criar o setter, nos utilizamos o decorador NomedoGetter.setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


p1 = Pessoa('Thiago', 'Mares')
p1.nome = "Gustavo"
print(p1.nome)