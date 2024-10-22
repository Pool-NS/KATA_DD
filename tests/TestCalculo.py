import unittest
from src.logica.calculo import calcular_promedio,NoSePuedeCalcular

class TestCalculoPromedio(unittest.TestCase):

    def test_lista_vacia(self):
        # Lista vacía debe lanzar NoSePuedeCalcular
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_un_solo_elemento(self):
        # Un solo elemento en la lista
        self.assertEqual(calcular_promedio([5]), 5)

    def test_dos_elementos(self):
        # Dos elementos en la lista
        self.assertEqual(calcular_promedio([5, 15]), 10)

    def test_n_elementos_positivos(self):
        # Números positivos en la lista
        self.assertEqual(calcular_promedio([2, 4, 6, 8]), 5)

    def test_todos_ceros(self):
        # Todos ceros en la lista
        self.assertEqual(calcular_promedio([0, 0, 0, 0]), 0)

    def test_elementos_positivos_y_negativos(self):
        # Números positivos y negativos
        self.assertEqual(calcular_promedio([3, -3, 3, -3]), 0)

    def test_elementos_no_numericos(self):
        # Elementos no numéricos deben lanzar TypeError
        with self.assertRaises(TypeError):
            calcular_promedio([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()