class NoSePuedeCalcular(Exception):
    """Excepción personalizada para errores en el cálculo."""
    pass

class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto) == 0:
            raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía.")
        return sum(self.__conjunto) / len(self.__conjunto)  # Aquí está la corrección











