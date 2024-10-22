import unittest
from src.logica.Conjunto import Conjunto, NoSePuedeCalcular

class TestCalculoPromedio(unittest.TestCase):

    def test_conjunto_vacio_lanza_excepcion(self):
        # Lista vacía debe lanzar NoSePuedeCalcular
        conjunto = Conjunto([])
        with self.assertRaises(NoSePuedeCalcular):
            conjunto.promedio()

    def test_un_solo_elemento(self):
        # Un solo elemento en la lista
        conjunto = Conjunto([5])
        self.assertEqual(conjunto.promedio(), 5)


    def test_dos_elementos(self):
        # Dos elementos en la lista
        conjunto = Conjunto([5, 15])
        self.assertEqual(conjunto.promedio(), 10)

    def test_n_elementos_positivos(self):
        # Números positivos en la lista
        conjunto = Conjunto([2, 4, 6, 8])
        self.assertEqual(conjunto.promedio(), 5)

    def test_todos_ceros(self):
        # Todos ceros en la lista
        conjunto = Conjunto([0, 0, 0, 0])
        self.assertEqual(conjunto.promedio(), 0)

    def test_elementos_positivos_y_negativos(self):
        # Números positivos y negativos
         conjunto = Conjunto([3, -3, 3, -3])
        self.assertEqual(conjunto.promedio(), 0)

if __name__ == '__main__':
    unittest.main()













