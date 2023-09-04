import unittest
from Atividades import comer

class AtividadesTestes(unittest.TestCase):
    
    def teste_comer(self):
        """E é sempre bom deixar claro em docstrings o que aquele testes está se tratando"""
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
