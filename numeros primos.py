lista1 = list()

for n in range(1, 999, 1):
    if n % (n+1) == 0:
        print(n)
        while teste < 9999:
            lista1.append(n)
            teste = teste + 1
    print(lista1)