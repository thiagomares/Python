"""
    Fazendo uso de anotations
    
    Annotations nos ajudam a usar type hints, quando nos utilizamos, por exemplo: nomedavar: tipodavar
    
    # Forma correta

    texto: str
    def cumprimentar(nome: str) -> str: # Deve se manter espaço entre o arrow e o tipo da saida
        return nome


    # Forma correta

    texto:str
    texto : str
    
    
    Quando nos utilizamos o método mágico annotations em um método ou função, ele mostra as anotações da função ou da classe, e qunado usamos sozinho, ele retorna todos os tipos para todas as variáveis declaradas no arquivo
"""

# Forma correta

texto: str
def cumprimentar(nome: str) -> str: # Deve se manter espaço entre o arrow e o tipo da saida
    return nome

print(cumprimentar.__annotations__)

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso
    
    def andar(self) -> str:
        return f'{self.__nome} está andando'
    

p = Pessoa(nome="Thiago", idade=28, peso=105.1)
print(p.andar.__annotations__)
