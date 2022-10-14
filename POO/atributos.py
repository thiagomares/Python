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

    @tensao.setter  # e para criar um setter, basta usar o @nomedaclasse.setter
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

        def retornaNome(self):
            return self.__name
# Então, para prevenir o acesso (lembrando que ele não proibe o acesso, apenas dificulta) o python une o nome da classe com o nome do atributo, como _Privado__age


# Os atributos podem ser publicos ou privados. A gente vai definir se um atributo é privado, é o name mangling; Para acessar esse atributo, nos devemos utilizar do jeito que escrevi
privado = Privado("Thiago", 27)
print(privado._Privado__name)  # Lembre-se: não é o ideal acessar dessa forma.

# Atributos de instancia
# Quando criamos instancias de uma classe, todas as instancias terão estes atributos


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def mostraSenha(self):
        return self.senha

    def mostraEmail(self):
        return self.email


user1 = Acesso('thiagofmares@outlook.com', 1234465)
user2 = Acesso('thiago.mares@outlook.com', 1123321)

# Atributos de classe
# Sao atributos de classe são atributos declarados diretamente na classe, fora da classe construtora, inicializada com um valor, e esse valor é compartilhado entre todas as instancias da classe. Ao invés de cada instancia da classe ter seus prórios valores, como os atributos de instancia, com os atributos de classe, todas as instancias terão um valor padrão;

# Refatorando o acesso...


class Acesso:
    # Atributo de classe
    # No C#, seriam aquelas variaveis public int...
    imposto = 1.05
    contador = 0

    # Atributo de instancia
    def __init__(self, produto, valor):
        self.id = Acesso.contador + 1
        self.produto = produto
        # para acessar os atributos da classe, temos que declarar a classe nele
        self.valor = (valor * Acesso.imposto)
        Acesso.contador = self.id  # Fazemos isso para que o contador conte automaticamente o id


produto = Acesso('PS5', 3000)
produto.imposto = 1.24
print(produto.contador)


# Atributos dinamicos
# Atributos de instancia são atributos criados em runtime
# Atributos de instancia são atributos que são definidos pelo programador. O atributo de dinamico será exclusivo da instancia que o criou

p1 = Acesso('ps2', 300)
p2 = Acesso('ps3', 1200)

# Criando o atributo dinamico em realtime
p2.peso = 5

# O que nos vemos aqui: Como p1 não tem  o atributo dinamico, o python vai levantar o erro, por isso o try-except-finally, e como p2 gera um atributo dinamicamente, ou seja, o atributo nao existe na classe abstrata e somente no objeto p2, somente esse vai ter esse atributo
try:
    print(p1.peso, p2.peso)
except:
    pass
finally:
    print(p2.peso)

#  Deletando atributos
del p2.peso
print(p2.peso)
