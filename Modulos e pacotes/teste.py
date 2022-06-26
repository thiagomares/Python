from classes import Teste

class Retorno(Teste):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome) # Herança

    def ola_mundo(self):
        print(self._sobrenome)

    teste_original = Teste.teste # Método para fazer um alias

    def teste(self): # Polimorfismo
        return ('Módulo teste')



if __name__ == '__main__': # Se não colocarmos isso aqui, o codigo vai colocar o print quando for importado para outro script
    print('Olá mundo')
