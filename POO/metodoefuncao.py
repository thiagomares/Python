class Metodo:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def retorna_nome(self):
        return f'{self.nome} {self.sobrenome}'

def funcao(nome, sobrenome):
    return f'{nome} {sobrenome}'

p1 = funcao('Thiago', 'Mares')
p2 = Metodo('Thiago', 'Mares')

print(p1)
print(p2.retorna_nome())
