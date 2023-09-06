''' 
    Hooks - Antes e apos hooks
    
    São os testes em si
    
    setup () = é executado antes de cada método de teste. é util para criarmos instancias de objetos e outros dados
    
    tearDown - é executado ao final de cada método de teste. é util para excluir dados ou fechar conexões com bancos de dados
    
'''

import unittest


class ModuloTest(unittest.TestCase):
    def setUp(self):
        # Método de configuração do setUp
        pass

    def test_primeiro(self):
        # SetUp vai rodar antes do teste
        # tearDown() vai rodar depois do teste
        pass

    def test_segundo(self):
        # SetUp vai rodar antes do teste
        # tearDown() vai rodar depois do teste
        pass

    def tearDown(self):
        # metodo de configuração do teardown
        pass

