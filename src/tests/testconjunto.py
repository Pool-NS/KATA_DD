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


if __name__ == '__main__':
    unittest.main()













