    """Esta función calcula la conversión entre diferentes unidades de medida kilogramos a libras, gramos a onzas, kilogramos a toneladas"""
    """ Esta funcion realiza la conversion entre kilogramos a libras """ 
    def kilogramos_libras(kg):
        z = kg * 2.20462
        return z
    """Esta función convierte una cantidad de gramos a onzas mediante un valor de conversión establecido"""
    def Gramos_onzas(g):
        z = g * 0.035274 
        return z
    """Esta función convierte una cantidad de kilogramos a toneladas dividiendo el valor entre mil"""
    def kilogramos_toneladas(kg):
        z = kg / 1000
        return z