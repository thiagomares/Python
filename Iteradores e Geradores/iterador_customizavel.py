"""
    Escrevendo um iterador customizado


"""

# Um range comum
from mimetypes import init


for n in range(0, 11):
    print(n)

# Criando nosso contador
class Contador:
    def __init__(self, menor, maior):
        self.maior = maior
        self.menor = menor
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Contador(1, 61)
it = iter(con)
print(next(it))
print(next(it))

if __name__ == "__main__":
    pass

