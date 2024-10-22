import unittest
import math
from src.logica.calculo import calcular_promedio, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculoPromedio(unittest.TestCase):
    def test_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_un_solo_elemento(self):
        self.assertEqual(calcular_promedio([5]), 5)

    def test_dos_elementos(self):
        self.assertEqual(calcular_promedio([10, 20]), 15)

    def test_n_elementos_positivos(self):
        self.assertEqual(calcular_promedio([2, 4, 6, 8]), 5)

    def test_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_promedio([1, 'a', 3])

    def test_elementos_decimales(self):
        self.assertAlmostEqual(calcular_promedio([1.5, 2.5, 3.5]), 2.5)


class TestCalculoDesviacionEstandar(unittest.TestCase):
    def test_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_un_solo_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0)

    def test_dos_elementos(self):
        self.assertEqual(calcular_desviacion_estandar([5, 15]), 5)

    def test_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([1, 'a', 3])

    def test_elementos_decimales(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1.5, 2.5, 3.5]), math.sqrt(2 / 3), places=4)



    def test_lista_con_numeros_negativos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([-1, -2, -3]), math.sqrt(2 / 3), places=4)


class TestNoSePuedeCalcular(unittest.TestCase):
    def test_mensaje_error(self):
        mensaje = "Error de prueba"
        excepcion = NoSePuedeCalcular(mensaje)
        self.assertEqual(str(excepcion), mensaje)

    def test_raise_exception(self):
        with self.assertRaises(NoSePuedeCalcular):
            raise NoSePuedeCalcular("Error de prueba")


if __name__ == '__main__':
    unittest.main()
