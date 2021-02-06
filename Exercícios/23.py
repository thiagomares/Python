# Fazer com que o codigo receba o valor e calcule 1/n!

fatorial = 0
somatorio = 0.0
VariavelControle = 0
numerobase = 1
fatorial = input("Digite o numero fatorial que deseja calcular")
for r in fatorial:
    if somatorio > 0:
        for controle in fatorial:
            VariavelControle = VariavelControle * r
            somatorio = numerobase / VariavelControle
        print (somatorio)

    elif somatorio == 0:
        somatorio += 1

print(somatorio)