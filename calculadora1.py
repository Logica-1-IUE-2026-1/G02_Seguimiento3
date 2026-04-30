"""Calculadora con librerias"""
import dividir
import os
import time
import logging

logging.basicConfig(
    filename='Mylog.log',
    level=logging.DEBUG,    # Nivel de logging
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato del mensaje
    datefmt='%Y-%m-%d %H:%M:%S' # Formato de la fecha y hora
)

def main():
    """
    Función principal que ejecuta la división de dos números.
    """
    logging.info("---Iniciando ejecución---")
    x=0
    logging.debug("El valor de x es %s",x)
    y=0
    logging.debug("El valor de y es %s",y)
    while y==0:
        print("-" * 11)
        print("Bienvenido a la calculadora")
        try:
            logging.info("Solicitar números a usuario")
            x=float(input("Ingrese número 1: "))
            logging.debug("El valor de x es %s",x)
            y=float(input("Ingrese número 2: "))
            logging.debug("El valor de y es %s",y)
            if y==0:
                logging.warning("Se ingreso invalido para el denominador")
                print("Valor invalido")
                time.sleep(2)
                os.system("cls")
        except:
            logging.error("Valores invalidos por usuario")
            print("Mongolo")
            time.sleep(2)
            os.system("cls")

    logging.info("Iniciando división")
    divisionxy=dividir.division(x,y)
    print(f'La división de {x} / {y} es: {divisionxy}')
    logging.debug("El resultado de la división es %s",divisionxy)
    return 0

if __name__=="__main__":
    os.system("cls")
    RESULT = main()
    if RESULT == 0:
        print("Resultado de la ejecución es exitoso")
        logging.info("---Finaliza ejecución exitosamente---")
    else:
        print("Resultado de la ejecución es fallido")
        logging.info("---Finaliza ejecución con error---")
