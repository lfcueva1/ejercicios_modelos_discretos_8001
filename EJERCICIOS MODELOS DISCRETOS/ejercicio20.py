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
    print("Ingrese el valor del radio de la esfera: ",end="")
    radio = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(radio<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        radio = validar_numeros_flotantes()
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
            print("No ha ingresado un numero,ingrese de nuevo:",end="")
    return numero
def calcular_volumen_esfera(radio):
    '''
    Funcion que calcula el volumen de una esfera

    Parametros:
    ------------
        radio : floar

    Retorna:
    ------------
        volumen : float
    '''
    #calculo el volumen de la esfera
    volumen = (4/3)*math.pi*(radio**3)
    return volumen
if __name__ == '__main__':
    #leo variables
    radio=leer_variables()
    #imprimo el volumen de la esfera
    print("El volumen de la esfera es: ",calcular_volumen_esfera(radio))
