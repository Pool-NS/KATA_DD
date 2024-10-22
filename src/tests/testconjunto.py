import unittest
from src.logica.calculo import calcular_promedio,NoSePuedeCalcular

class TestCalculoPromedio(unittest.TestCase):

    def test_lista_vacia(self):
        # Lista vacía debe lanzar NoSePuedeCalcular
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

if __name__ == '__main__':
    unittest.main()











