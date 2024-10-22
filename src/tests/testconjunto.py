import unittest
from src.logica.Conjunto import Conjunto, NoSePuedeCalcular

class TestCalculoPromedio(unittest.TestCase):

    def test_lista_vacia(self):
        # Lista vacía debe lanzar NoSePuedeCalcular
        conjunto = Conjunto([])
        with self.assertRaises(NoSePuedeCalcular):
            conjunto.promedio()

if __name__ == '__main__':
    unittest.main()











