class Robo:
    def __init__(self, name, bateria=100, habilidades=[]):
        self.__name =  name
        self.__bateria = bateria
        self.__habilidades = habilidades
    
    @property
    def name(self):
        return self.__name
    
    @property 
    def bateria(self):
        return self.__bateria
    
    @property
    def habilidades(self):
        return self.__habilidades
    
    @name.setter
    def name(self, nome):
        self.__name = nome
    
    @bateria.setter
    def bateria(self, capacidade):
        self.__bateria = capacidade
    
    @habilidades.setter
    def habilidades(self, habilidades):
        self.__habilidades.append(habilidades)
    
    def carregar(self):
        self.__bateria = 100
        return self.__bateria
    
    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria =- 1
            return f'Olá, mundo! Eu sou {self.name}'
        return "Sem carga"
    
    def nova_habilidade(self, habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria =- custo
            self.__habilidades.append(habilidade)
        
bot = Robo(name="Thiago")
bot.bateria = 200
print(bot.name)
