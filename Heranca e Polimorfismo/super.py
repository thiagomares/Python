"""
    O método super

    O Método super serve para acessarmos de forma pythonica a super classe (a classe pai)
"""

class Pai:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

    def diz_oi(self):
        return "oi"

class Filha(Pai):
    def __init__(self, nome, sobrenome, telefone):
        super().__init__(nome, sobrenome)
        self.__telefone = telefone

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

p1 = Filha("Thiago", "Mares", 31989190738)
print(p1.diz_oi())
p1.telefone = 3135825881
print(p1.telefone)
