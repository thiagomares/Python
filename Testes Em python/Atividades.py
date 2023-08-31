''' 
    Introdução ao módulo de Unittest (teste unitário)
    
    O que são testes unitários: é uma forma de se testar unidades individuais de um código, como uma classe, método, ou função...
    
    O Objetivo dos testes unitarios é verificar o funcionamento correto daquela unidade testada
    
    OBS: teste unitario não é especifico da linguagem python.
    Para Criar nossos testes, criamos classes que herdam de unittest.testcase e a partir de então ganhamos todos os assertions presentes no módulo
    
    E para rodar os teste, utilizamos o unittest.main()
    
    O arquivo de teste é um arquivo separado
    
    # Conhecendo as assertions
        AsserrtEqual(a,b) => a ==b
        assertNotEqual(a,b) => a!=b
        assertTrue(x) => x é verdadeiro
        assertFalse(x) => x é falso
        assertIs(a, b) => a é b
        assertIsNot(a, b) => A não é b
        assertIsNone(x) => X é none
        assertIsNotNone(x) => X não é none
        assertIn(a,b) => a está em b
        assertNotIn(a, b) => a nao está em b
        assertIsInstance(a,b) => a é instancia de b
        assertNotIsInstance(a, b) => a não é instancia de b
'''

# Utilizando a abordagem tdd

def comer(comida, saudavel):
    pass

def dormir(horas):
    pass

