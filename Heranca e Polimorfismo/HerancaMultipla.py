"""
    Herança Multipla nada mais é que a possibilidade de uma classe herdar de múltiplas classes,


    fazendo com que a classe filha


    herde todos os atributos e métodos de todas as classes herdadas


    A herança multipla pode ser feita de duas maneiras: por multiderivação direta ou por multiderivação indireta


"""
# Multiderivação direta


class Pai:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class Mae:
    def __init__(self, telefone):
        self.telefone = telefone


class Filha(Pai, Mae):
    def __init__(self, nome, sobrenome, telefone):
        super().__init__(nome, sobrenome, telefone)

    pass

# Multiderivação indireta


class Neta(Filha):
    pass
