
"""
    Esta es la función integradora que va a reunir todas las funciones 
    matematicas y las va a ejecutar pro medio de la función main
"""

import circulo
import cuadrado
import triangulo

def main():
    """

        Función principal que ejecuta la operaciones matematicas entre dos números
    """
    opcion = int(input("ingrese opcion(1:circulo 2:cuadrado 3:triangulo)"))

    if opcion == 1:

        # Primero vamos a llamar las operaciones del circulo
        print("Calculadora de areá y perimetro de diferentes formas\n")
        print("Vamos a iniciar con el Circulo")
        radio=int(input("Ingresa el radio\n"))#pedimos el radio del circulo

        area_circulo = circulo.area_circulo(radio)
        perimetro_circulo = circulo.perimetro_circulo(radio)

        print(f"el area del circulo es: {area_circulo}\n")
        print(f"el perimetro del circulo es: {perimetro_circulo}\n")

        # Segundo vamos a llamar las operaciones del cuadrado
    elif opcion == 2:
        print("Continua con el cuadrado\n")
        lado_cuadrado=int(input("Ingresa un lado del cuadrado\n"))#pedimos un lado del cuadrado

        area_cuadrado = cuadrado.area_cuadrado(lado_cuadrado)
        perimetro_cuadrado = cuadrado.perimetro_cuadrado(lado_cuadrado)

        print(f"el area del cuadrado es: {area_cuadrado}\n")
        print(f"el perimetro del circulo es: {perimetro_cuadrado}\n")

        # Tercero vamos a llamar las operaciones del triangulo
    else:
        print("Continua con el triangulo\n")
        altura_triangulo=int(input("Ingresa la altura del triangulo\n"))#pedimos la altura del triangulo
        base_triangulo=int(input("Ingresa la base del triangulo (lado 1)\n"))#pedimos la base del triangulo
        lado2_triangulo=int(input("Ingresa otro lado del triangulo (lado 2)\n"))#pedimos el lado 2 triangulo
        lado3_triangulo=int(input("Ingresa el tercer lado del triangulo (lado 3)\n"))#pedimos el lado 3 del triangulo

        area_triangulo = triangulo.area_triangulo(base_triangulo,altura_triangulo)
        perimetro_triangulo = triangulo.perimetro_triangulo(base_triangulo, lado2_triangulo, lado3_triangulo)

        print(f"el area del triangulo es: {area_triangulo}\n")
        print(f"el perimetro del triangulo es: {perimetro_triangulo}\n")

    return 0


if __name__== "__main__":
    RESULT = main()
    if RESULT == 0:
        print("Resultado de la ejecución es exitoso")
    else:
        print("Resultado de la ejecución es fallido")
