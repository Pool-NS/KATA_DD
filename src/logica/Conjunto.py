class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if not self.__conjunto:  # Si el conjunto está vacío
            return None
        return sum(self.__conjunto) / len(self.__conjunto)  # Calcular el promedio
