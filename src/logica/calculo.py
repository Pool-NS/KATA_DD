import math


class NoSePuedeCalcular(Exception):
    """Excepción personalizada para errores en el cálculo."""
    pass


def calcular_promedio(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía.")

    for elemento in elementos:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser números.")

    return sum(elementos) / len(elementos)


def calcular_desviacion_estandar(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía.")

    for elemento in elementos:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser números.")

    promedio = calcular_promedio(elementos)
    varianza = sum((x - promedio) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)
