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
        centimetro : float
    '''
    #inicializo la variable numero1 a cero
    numero1 = 0
    #solicito al usuario que ingrese la variable numero1
    print("Ingrese numero 1: ",end="")
    numero1 = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(numero1<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        numero1 = validar_numeros_flotantes()
    #retornamos la o las variables
    return numero1
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

def calcular_raiz_cuadrada(numero1):
    '''
    Funcion que calcula la raiz cuadrada de cualquier numero

    Parametros:
    ------------
        numero1 : float

    Retorna:
    ------------
        raizCuadrada : float
    '''
    #calculo la raiz cuadrada
    raizCuadrada = math.sqrt(numero1)
    #retorno el resultado
    return raizCuadrada
if __name__ == '__main__':
    #leo la variable
    numero1=leer_variables()
    #imprimo el resultado de la raiz cuadrada
    print("La raiz cuadrada de ",numero1," es: ",calcular_raiz_cuadrada(numero1))
