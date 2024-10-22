# archivo: testdesviacion/test_desviacion.py

import unittest
from src.logica.desviacion import DesviacionEstandar, NoSePuedeCalcular

class TestDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            DesviacionEstandar.calcular([])

    def test_un_elemento(self):
        self.assertEqual(DesviacionEstandar.calcular([5]), 0.0)

    def test_dos_elementos(self):
        self.assertAlmostEqual(DesviacionEstandar.calcular([4, 6]), 1.0)

    def test_varios_elementos_positivos(self):
        self.assertAlmostEqual(DesviacionEstandar.calcular([1, 2, 3, 4, 5]), 1.4142135623730951)

    def test_varios_elementos_todos_ceros(self):
        self.assertEqual(DesviacionEstandar.calcular([0, 0, 0]), 0.0)

    def test_varios_elementos_positivos_y_negativos(self):
        self.assertAlmostEqual(DesviacionEstandar.calcular([-1, 0, 1]), 0.816496580927726)

    def test_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            DesviacionEstandar.calcular([1, 'a', 3.5])

if __name__ == "__main__":
    unittest.main()
