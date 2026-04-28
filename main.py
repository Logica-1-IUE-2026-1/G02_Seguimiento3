"""
    función integradora con función de menu
"""
import sys
import seguimiento3
import temperatura


def menu():
    """
<<<<<<< Updated upstream
        Esta es la función que va a funcionar como menu
=======
        Esta es la función que va a funcionar como menu dr dos niveles
>>>>>>> Stashed changes
    """
    print("¡Bienvenido! \n ¿Que desea hacer?\n" \
        "1) Convertir masas\n"\
        "2) Convertir temperaturas\n"\
        "3) Salir" )

    var = int(input(""))

    while var <= 3 and var >= 1:
        if var == 3:
            sys.exit()
        elif var == 2:
            print("¿Como desea convertir la temperatura?\n" \
                "1) celsius a fahrenheit\n"\
                "2) fahrenheit a celsius\n"\
                "3) celsius a kelvin" )
            option = int(input(""))
            return option
        else:
            print("¿Como desea convertir las masas?\n" \
                "a) kilogramos a libras\n"\
                "b) gramos a onsas\n"\
                "c) kilogramos a toneladas" )
            option = str(input(""))
            return option
    return 0


def main():
    """
        función integradora
    """
    option_menu = menu()
    if option_menu == 1:
        print("Ingrese la cantidad a convertir")
        c = float(input(""))
        result = temperatura.celsius_a_fahrenheit(c)
        print(f"el valor es: {result}")
    elif option_menu == 2:
        print("Ingrese la cantidad a convertir")
        c = float(input(""))
        result = temperatura.fahrenheit_a_celsius(c)
        print(f"el valor es: {result}")
    elif option_menu == 3:
        print("Ingrese la cantidad a convertir")
        c = float(input(""))
        result = temperatura.celsius_a_kelvin(c)
        print(f"el valor es: {result}")
    elif option_menu == "a":
        print("Ingrese la cantidad a convertir")
        c = float(input(""))
        result = seguimiento3.kilogramos_libras(c)
        print(f"el valor es: {result}")
    elif option_menu == "b":
        print("Ingrese la cantidad a convertir")
        c = float(input(""))
        result = seguimiento3.gramos_onzas(c)
        print(f"el valor es: {result}")
    elif option_menu == 0:
        return 1
    else:
        print("Ingrese la cantidad a convertir")
        c = float(input(""))
        result = seguimiento3.kilogramos_toneladas(c)
        print(f"el valor es: {result}")

    return 0



if __name__== "__main__":
    RESULT = main()
    if RESULT == 0:
        print("Resultado de la ejecución es exitoso")
    else:
        print("Resultado de la ejecución es fallido")
