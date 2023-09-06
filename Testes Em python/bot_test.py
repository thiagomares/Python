import unittest
from bot import Robo

class RoboTestes(unittest.TestCase):
    def setUp(self):
        self.megaman = Robo('megaman', bateria=50)
    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)
        
    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), "Olá, mundo! Eu sou megaman")
        
    def tearDown(self):
        print('tearDown está sendo executado')

if __name__ == '__main__':
    unittest.main()
