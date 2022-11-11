"""
    Objetos

    São instancias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação na computação
    devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos de uma classe como variaveis do
    tipo definido na classe
"""

class Lampada:
    def __init__(self, cor, tensao, luminosidade):
        self.cor = cor
        self.tensao = tensao
        self.luminosidade = luminosidade
        self.ligada = False

    def liga_desliga(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def verificador(self):
        return self.ligada

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


nova_lampada = Lampada('verde', 110, 80)
nova_lampada.liga_desliga()
print(nova_lampada.verificador())
