# Atributos
""" 
    O que são atributos?
    
    Representam as características de um objeto, ou seja, pelos atributos nos conseguimos representar computacionalmente os estados de um objeto.
    
    Em python, dividimos os atributos em 3 grupos. Atributos de instancia, atributos de classe e atributos dinâmicos.
"""

# Atributo de instancia
""" 
    Aqui nos vamos ver um método de instância, que é o método init (método construtor)
    Método construtor: É um método especial que utilizamos para a construção do objeto
"""


class Lampada:
    def __init__(self, tensao, cor):
        self.tensao = tensao
        self.cor = cor
        self.condicao = False

        # Quando colocamos o dunder na variável no atributo de instancia, nos estamos falando que aquela variável é privada.

    # Quando criamos um @property, nos estamos criando um getter
    @property
    def tensao(self):
        return self.tensao

    @property
    def cor(self):
        return self.cor

    @property
    def condicao(self):
        return self.condicao
