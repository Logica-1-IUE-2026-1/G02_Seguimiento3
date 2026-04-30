"""
    Esta función calcula la conversión entre diferentes unidades
    de medida kilogramos a libras, gramos a onzas, kilogramos a toneladas
"""

def kilogramos_libras(kg):
    """ Esta funcion realiza la conversion entre kilogramos a libras """
    z = kg * 2.20462
    return z

def gramos_onzas(g):
    """Esta función convierte una cantidad de gramos a onzas"""
    z = g * 0.035274
    return z

def kilogramos_toneladas(kg):
    """
        Esta función convierte una cantidad de kilogramos a
        toneladas dividiendo el valor entre mi
    """
    z = kg / 1000
    return z

