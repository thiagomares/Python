""" 
    Métodos
    
    Métodos ou funções (def) representam os comportamentos do objeto. ou seja, as ações que este objeto pode realizar no sistema
    
    Em python, dividimos os métodos em dois grupos: métodos de instancia e métodos de classe
    
    O método __init__ é um método construtor, e serve para construir a nossa classe; Todo elemento dunder, e são chamados de métodos mágicos.add()


    Não usa faça a porra do dunder no sistema, ce pode cagar tudo nessa merda

    Métodos são escritos em lower case, e caso composto, é no esquema snake case
    


"""

# Métodos de instancia


class Lampada:
    def __init__(self, cor, tensao, luminosidade):
        self.cor = cor
        self.tensao = tensao
        self.luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.contador = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.contador

    # Porque método de instancia? Pois somente pode ser acessado se criado uma instancia para ele
    # exemplo: p1.nomeDaClasse, pois daí nos indicamos para o self que a instancia que ele tem que endereçar é o nome da instancia que a gente passou

    def desconto(self, porcentagem):
        """Calcula o valor com desconto"""
        return (self.valor * (1 - porcentagem/100))

    @classmethod
    def conta_produto(cls):
        return cls.contador

    # E assim como nos atributos, podemos ter também os métodos privados, que são declarados da mesma forma, com name mangling

    def __privado(self):
        return self.descricao

    # E por fim, nos temos os métodos estáticos
    @staticmethod
    def estatico():
        return 'Estático'


produto = Produto('PS5', 'videogame', 3500)
print(produto.desconto(23))

# Método de classe
# Diferente dos métodos de instancia, os métodos de classe dependem de um decorator, como o @classmethod...E no caso de class method, ao inves de utilizarmos self, utilizamos cls

print(Produto.conta_produto())

""" 
    Quando utilizar metodo de instancia ou usar método de classe?

    Quite simple: Utilizamos metodo de instancia quando queremos criar um objeto de uma classe para retornar um item necessário, como ações que aquele objeto vai ter, como desconto, acrescimo de um produto.
    
    Já os métodos de classe, é quando precisamos fazer operações dentro da própria classe
"""
