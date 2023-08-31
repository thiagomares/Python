''' 
    Assertions ( afirmações/checkagens ou questionamentos)
    
    Em python, utilizamos a palavra reservada assert para realizar simples afirmações utilizadas nos testes
    Utilizamos o 'assert' em uma expressao que queremos checar se é válida ou não.
    
    Se a expressão for verdadeira, o assert retorna None, e caso seja falsa, o assert levanta um erro do tipo AssertionError
    
    OBS: Nos podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada (assim como rola com try except?)
            A palavra assert pode ser usada em qualquer função ou codigo, nao precisa ser exclusivamente nos testes.
            
    Atenção: Cuidado ao usar o assert
    Se um programa python for executado com o parametro -o, nenhum assertion será validado, ou seja, todas as validações não vao funcionar 
'''

def soma_positivos(a,b):
    assert a>0 and b>0, 'ambos numeros precisam ser positivos'
    return a+b

ret  = soma_positivos(2,4)
print(ret)

# Outro Exemplo
def comer_porcaria(comida):
    assert comida in ['pizza', 'sorvete', 'doces', 'batata frita', 'sanduiches'], 'comida precisa ser fast food'
    return f'A comida precisa ser {comida}'

comida = comer_porcaria("salada")
print(comida)



