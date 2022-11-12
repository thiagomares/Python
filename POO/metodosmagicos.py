""" 
    Métodos mágicos são todos os métodos que utilizam dunder

    Exemplo: __init__
    
    __repr__ => representação de um objeto
"""


class Classe:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # Quando utilizamos o método str, ele sobrepoe o metodo de representação (meio que se torna inutil na verdade)
    def __str__(self):
        return "Olá, mundo"

    def __repr__(self):
        return f"{self.nome} {self.sobrenome}"


objeto = Classe('Thiago', 'Mares')
print(objeto)
