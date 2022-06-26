class Referencias:
    def teste():
        print('Olá Mundo')

    def outro(self, a, b): # Tem que lembrar da porra do self
        return a + b

a = Referencias()
print(a.outro(2**12, 2**10))