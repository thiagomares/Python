# Atributos
""" 
    O que são atributos?
    
    Representam as características de um objeto, ou seja, pelos atributos nos conseguimos representar computacionalmente os estados de um objeto.
    
    Em python, dividimos os atributos em 3 grupos. Atributos de instancia, atributos de classe e atributos dinâmicos.


    Em python, ficou estabelecido que todo atributo de uma classe é público! Ou seja, pode ser acessado em qualquer parte do projeto;
    Caso queiramos demonstrar que um atributo deve ser tratado como privado (utilizado somente dentro da classe), utiliza-se duplo underscore no inicio de seu nome, isso é conhecido como name mangling.
"""

# Atributo de instancia
"""     Aqui nos vamos ver um método de instância, que é o método init (método construtor)
    Método construtor: É um método especial que utilizamos para a construção do objeto
"""


class Lampada:
    def __init__(self, tensao, cor):
        self.__tensao = tensao
        self.__cor = cor
        self.__condicao = False

        # Quando colocamos o dunder na variável no atributo de instancia, nos estamos falando que aquela variável é privada.

    # Quando criamos um @property, nos estamos criando um getter
    @property
    def tensao(self):
        return self.__tensao

    @property
    def cor(self):
        return self.__cor

    @property
    def condicao(self):
        return self.__condicao
    
    @tensao.setter # e para criar um setter, basta usar o @nomedaclasse.setter
    def tensao(self, tensao):
        self.__tensao = tensao

    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    

# Quando utilizamos utilizamos a palavra reservada self, nos estamos indicando para o objeto atributos para ele

lampada = Lampada(110, "verde")
lampada.tensao = 220
lampada.cor = "Branca"
print(lampada.tensao)
print(lampada.cor)
""" Atributos publicos e privados """
""" 
    Em python, foi estabelecido que todo atributo são públicos. Caso determinado atributo tem que ser tratado como PRIVADO, que somente deve ser utilizado dentro da classe original, utiliza-se underscore no inicio do nome, isso é conhecido como name mangling.
"""


# Classe com atributo de instancia privado


class Privado:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
# Então, para prevenir o acesso (lembrando que ele não proibe o acesso, apenas dificulta) o python une o nome da classe com o nome do atributo, como _Privado__age


# Os atributos podem ser publicos, privados ou protegido

