def f(ham: str, eggs: str = 'eggs'):
    print("Annotations:", f.__annotations__)
    # print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

# Para verificarmos os argumentos da função, nos fazemos uma call da função interna .__annotations__
f('spam')


# Funçao enumerate: ele ennumera nossos elementos de uma lista, tupla ou conjunto
for i in enumerate(['a', 'b', 'c']):
    print(i)