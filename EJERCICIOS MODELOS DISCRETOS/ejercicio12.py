import os
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
    #inicializo la variable numero2 a cero
    numero2 = 0
    #solicito al usuario que ingrese la variable numero1
    print("Ingrese numero 1: ",end="")
    numero1 = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable numero2
    print("Ingrese numero 2: ",end="")
    numero2 = validar_numeros_flotantes()
    #retornamos la o las variables
    return numero1,numero2
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

def calcular_suma(numero1,numero2):
    '''
    Funcion que calcula la suma de dos numeros

    Parametros:
    ------------
        numero1 : float
        numero2 : float

    Retorna:
    ------------
        suma : float
    '''
    #calculamos la suma
    suma = numero1+numero2
    #retornamos suma
    return suma
def calcular_resta(numero1,numero2):
    '''
    Funcion que calcula la resta de dos numeros

    Parametros:
    ------------
        numero1 : float
        numero2 : float

    Retorna:
    ------------
        resta : float
    '''
    #calculamos la resta
    resta = numero1-numero2
    #retornamos resta
    return resta
def calcular_multiplicacion(numero1,numero2):
    '''
    Funcion que calcula la multiplicacion de dos numeros

    Parametros:
    ------------
        numero1 : float
        numero2 : float

    Retorna:
    ------------
        multiplicacion : float
    '''
    #calculamos la multiplicacion
    multiplicacion = numero1*numero2
    #retornamos multiplicacion
    return multiplicacion
def calcular_division(numero1,numero2):
    '''
    Funcion que calcula la division de dos numeros

    Parametros:
    ------------
        numero1 : float
        numero2 : float

    Retorna:
    ------------
        division : float
    '''
    #calculamos la multiplicacion
    division = numero1/numero2
    #retornamos division
    return division
def calcular_exponencial(numero1,numero2):
    '''
    Funcion que calcula el exponencial con dos numeros

    Parametros:
    ------------
        numero1 : float
        numero2 : float

    Retorna:
    ------------
        exponencial : float
    '''
    #calculamos la exponencial
    exponencial = numero1**numero2
    #retornamos division
    return exponencial
    
if __name__ == '__main__':
    numero1,numero2=leer_variables()
    #imprimimos las operaciones aritmeticas
    print("Suma: ",calcular_suma(numero1,numero2))
    print("Resta: ",calcular_resta(numero1,numero2))
    print("Multiplicacion: ",calcular_multiplicacion(numero1,numero2))
    print("Division: ",calcular_division(numero1,numero2))
    print("Exponencial: ",calcular_exponencial(numero1,numero2))