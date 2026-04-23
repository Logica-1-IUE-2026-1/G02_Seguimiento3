"codigo de conversiones de temperatura"

def celsius_a_fahrenheit(c):
    """converte grados celsius a farenheit
    c (float): temperatura en grados celsius que se quiere convertir
    return: float: temperatura convertida en farenheit"""

    z = (c * 9/5) + 32 
    return z

def fahrenheit_a_celsius(f):
    """convierte grados farenheit a celsius
    f (float): temperatura en grados farenheit que se quiere convertir
    return: float: temperatura convertida en celsius
    """
    e = (f-32) * 5/9
    return e
def celsius_a_kelvin(c):
    """convierte grados celsius a kelvin
    c (float): temperatura en grados celsius que se quiere convertir
    return: float: temperatura convertida en kelvin
    """
    f = c + 273.15
    return f


