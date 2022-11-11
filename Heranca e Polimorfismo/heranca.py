"""
    Herança - Inheritance

    Herança é a possibilidade de reaproveitar codigos/classes e também extender nossas classes.

    Com a herança, a partir de uma classe existente, nos extendemos outra classe, nos passamos a herdar atributos e métodos da
    classe herdada
"""
# Herança Basica

class Pai:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def retona_nome(self):
        return f'{self.nome} {self.sobrenome}'

class Mae:

    def retorno(self, teste):
        return teste

class Filha(Pai, Mae):

    # Aqui nos temos uma especie de overload do método init, que tá recebendo um super dos atributos da classe pai
    def __init__(self, nome, sobrenome,  telefone):
        super().__init__(nome, sobrenome)
        self.telefone = telefone

    # Aqui nos estamos fazendo um overwrite do método herdado da classe Mãe, para que fique claro o que vamos herdar
    # Polimorfismo e overload no mesmo método kkk
    def retorno(self):
        return super().retona_nome()

    def retorna_telefone(self):
        return self.telefone

p1 = Filha("Thiago", "Mares", 31989190738)
print(p1.retona_nome())
print(p1.retorno())
