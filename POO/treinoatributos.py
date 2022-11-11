class Produtos:
    # Class attributes
    imposto = 1.2
    contador = 0

    # Instance Attributes
    def __init__(self, produto, preco, descricao):
        self.produto = produto
        self.preco = preco
        self.descricao = descricao
        self.id = Produtos.contador + 1
        Produtos.contador = self.id

    # Getters and setters
    @property
    def produto(self):
        return self.produto

    @property
    def preco(self):
        return self.preco

    @property
    def descricao(self):
        return self.descricao

    @property
    def imposto(self):
        return Produtos.imposto

    def imposto(self, valor):
        Produtos.imposto = valor

    def produto(self, valor):
        self.produto = valor

    def preco(self, valor):
        self.preco = valor

    def descricao(self, valor):
        self.descricao = valor

    # Methods
    def valorImposto(self):
        return (self.preco * (1 + self.imposto/100))


p1 = Produtos('Playstation 5', 5000, 'Video Game de ultima geração')
p1.aumenta = 30  # Dynamic attribute
p1.imposto = 40
print(p1.valorImposto() * (1 - p1.aumenta/100))
