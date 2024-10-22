

class NoSePuedeCalcular(Exception):
    """Excepción personalizada para errores de cálculo."""
    pass


class DesviacionEstandar:
    @staticmethod
    def calcular(lista):
        if not lista:
            raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía.")

        if len(lista) == 1:
            return 0.0

        for item in lista:
            if not isinstance(item, (int, float)):
                raise TypeError("La lista contiene elementos no numéricos.")

        media = sum(lista) / len(lista)
        varianza = sum((x - media) ** 2 for x in lista) / len(lista)
        return varianza ** 0.5
