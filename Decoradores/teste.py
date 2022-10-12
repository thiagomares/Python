def numero():
    for i in range(1, 11):
        yield i
        
numeroYield = numero()
print(next(numeroYield))
print(next(numeroYield))
print(next(numeroYield))