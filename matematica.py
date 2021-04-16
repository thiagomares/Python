import math
"""
    Estas são algumas operações que a biblioteca math do python pode fazer
"""

# Fazendo um MDC
print(math.gcd(2, 1024))

# Achando a hipotenusa de um triangulo retângulo
print(math.hypot(20, 40))


# Logarítmo em qualquer base
print(math.log(1024, 2))
# No caso acima, nos estaremos fazendo pegando o valor do logaritmando em primeiro e em seguida a base do logaritmo


# Logaritmo na base 10
print(math.log10(math.e))

# Seno, Cosseno e Tangente
print(math.cos(2), math.sin(2), math.tan(1/2))

# # Arco Seno, arco cosseno, arco tangente
# print(math.acos(math.pi), math.asin(math.pi), math.atan(math.pi))

# Convertendo um valor em radianos em graus
print(math.degrees(2 * math.pi))

# Convertendo um valor em graus para radianos
print(math.radians(180))
