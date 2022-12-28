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
        lados : float
        altura : float
    '''
    #inicializo la variable ancho a cero
    lados = 0
    #inicializo la variable altura a cero
    altura = 0
    #solicito al usuario que ingrese el ancho de la piramide
    print("Ingrese el valor de los lados del rectangulo: ",end="")
    lados = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(lados<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        lados = validar_numeros_flotantes()
    #solicito al usuario que ingrese la altura de la piramide
    print("Ingrese el valor de la altura del rectangulo: ",end="")
    altura = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(altura<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        altura = validar_numeros_flotantes()
    #retornamos la o las variables
    return lados,altura
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

def calcular_arista_lateral_de_piramide(lados,altura):
    '''
    Funcion que calcula la arista de una piramide con la ayuda de los catetos

    Parametros:
    ------------
        lados : float
        altura : float

    Retorna:
    ------------
        arista : float
    '''
    #Calculo la diagonal
    diagonal =(lados**2)+(lados**2)
    diagonal= math.sqrt(diagonal)
    #calculo semidiagonal / cateto
    semiDiagonal = diagonal/2
    cateto1=semiDiagonal
    cateto2= altura
    #calculo la arista
    incognitaArista = (cateto1**2) + (cateto2**2)
    arista = math.sqrt(incognitaArista)
    #retornamos el valor de la arista
    return arista

if __name__ == '__main__':
    lados,altura=leer_variables()
    print("La arista de la piramide es: ",calcular_arista_lateral_de_piramide(lados,altura))