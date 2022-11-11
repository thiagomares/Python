"""
    Abstração e encapsulamento

    O grande objetivo do POO é encapsular nosso codigo dentro de um grupo lógico e hierárquico utilizando classes.

    Encapsular => Cápsula => ato de guardar os elementos de uma classe.

    Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário
    
    Exemplo: quando temos um método que não pode ser acessado pela instancia, nos utilizamos a abstração para que este método não seja acessado
"""
import sqlite3
class Financeiro:
    conector = sqlite3.connect('bancodedados.db')

    
    def __init__(self, conta, saldo, nome):
        self.__conta = conta
        self.__saldo = saldo
        self.__nome = nome
        self.__cursor = Financeiro.conector.cursor()
    
    def verifica_nome(self):
        account = self.__cursor.execute("Select Conta from DadosBasicos")

