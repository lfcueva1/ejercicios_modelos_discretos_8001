import os
import math
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        radio : float
    '''
    #inicializo la variable radio a cero
    radio = 0
    #solicito al usuario que ingrese la variable radio
    print("Ingrese el valor del radio del circulo: ",end="")
    radio = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(radio<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        radio = validar_numeros_flotantes()
    #retornamos la o las variables
    return radio
def validar_numeros_flotantes():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es flotante, si lo que se ingresó no es un numero
    flotante entonces el usuario tendra que volver a ingresar un numero

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        numero : float
    '''
    #mientras sea verdadero se ingresara un dato en la variable numero, si lo que se ingreso es un numero flotante
    #rompera el ciclo repetitivo while sino el usuario debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=float(input())
            #rempemos ciclo repetitivo
            break
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
def calcular_area_circulo(radio):
    '''
    Funcion que permite calcular el area del circulo

    Parametros:
    ------------
        radio : float

    Retorna:
    ------------
        area : float
    '''
    #calculo el area del circulo con la siguiente formula
    area = math.pi*(radio**2)
    return area
if __name__ == '__main__':
    radio=leer_variables()
    #imprime area del circulo
    print("El area del circulo es: ",calcular_area_circulo(radio))
