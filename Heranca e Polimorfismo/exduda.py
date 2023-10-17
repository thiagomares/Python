class OlaPessoa:
    def __init__(self, nome):
        self.nome = nome

    def retorna_nome(self):
        return f'Olá {self.nome}'

if __name__ == "__main__":
    pessoa = OlaPessoa('Duda')
    print(pessoa.retorna_nome())
