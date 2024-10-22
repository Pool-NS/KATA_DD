class NoSePuedeCalcular(Exception):
    """Excepción personalizada para errores en el cálculo."""
    pass


def calcular_promedio(elementos):
    if not elementos:
        # Caso lista vacía
        raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía.")

    # Verificar si todos los elementos son numéricos
    for elemento in elementos:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser números.")

    # Calcular el promedio
    return sum(elementos) / len(elementos


