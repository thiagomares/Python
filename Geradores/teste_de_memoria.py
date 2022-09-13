# Teste de Memória

""" Este é um teste de desempenho do python utilizando python """


# Utilizando função comum

def fibonacci(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a = b
        b = a + b
    return nums
        


# Usando geradores

def gen_fibonacci(max):
    contador = 0
    a, b = 0,1
    while contador <= max:
        a = b
        b = a + b
        yield a
        contador += 1
        
for i in gen_fibonacci(100):
    print(i)
    
""" 
    Conclusão do teste:
    
    função geradoras utilizam muito menos memoria de processamento. Enquanto return utiliza 500 mb de memoria de processamento, a função geradora utiliza somente 2 MB
"""
