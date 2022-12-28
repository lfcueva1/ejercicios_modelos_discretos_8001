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
        a : float
        b : float
        c : float
    '''
    #inicializo la variable a,b y c a cero
    a = 0
    b = 0
    c = 0
    #solicito al usuario que ingrese la variable a
    print("Ingrese el valor de la variable a: ",end="")
    a = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable b
    print("Ingrese el valor de la variable b: ",end="")
    b = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable c
    print("Ingrese el valor de la variable c: ",end="")
    c = validar_numeros_flotantes()
    #retornamos la o las variables
    return a,b,c
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
def resolver_ecuacion(a,b,c):
    '''
    Funcion que resuelve la ecuacion

    Parametros:
    ------------
        a : int
        b : int
        c : int

    Retorna:
    ------------
        y
    '''
    #resuelvo la ecuacion
    y=(-b+(math.sqrt((b**2)+c)))/(2*a)
    #retorno y
    return y
if __name__ == '__main__':
    #leo variables
    a,b,c=leer_variables()
    #imprimo el resultado
    print("La ecuacion resuelta es y= ",resolver_ecuacion(a,b,c))