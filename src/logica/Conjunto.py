class NoSePuedeCalcular(Exception):
    """Excepción personalizada para errores en el cálculo del promedio."""
    pass


class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto) == 0:
            raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía.")
        if not all(isinstance(x, (int, float)) for x in self.__conjunto):
            raise TypeError("Todos los elementos deben ser números.")

        return sum(self.__conjunto) / len(self.__conjunto)





