import unittest
from Atividades import comer, dormir

class AtividadesTestes(unittest.TestCase):
    
    def teste_comer(self):
        self.assertEqual(
            comer("quiabo", True),
            "estou comendo quiabo porque eu gosto"
        )
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'eu vou morrer mesmo'
        )

if __name__ == "__name__":
    unittest.main()
