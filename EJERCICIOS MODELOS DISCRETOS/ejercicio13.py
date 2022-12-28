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
    numero1 = validar_numeros_enteros()
    #solicito al usuario que ingrese la variable numero2
    print("Ingrese el grado del exponente: ",end="")
    numero2 = validar_numeros_enteros()
    #retornamos la o las variables
    return numero1,numero2
def validar_numeros_enteros():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        numero : int
    '''
    #mientras sea verdadero se ingresara un dato en la variable numero, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el usuario debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=int(input())
            #rempemos ciclo repetitivo
            break
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
def calcular_exponencial_de_cualquier_numero(numero1,numero2):
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero

    Parametros:
    ------------
        numero1 : int
        numero2 : int

    Retorna:
    ------------
        exponencial : int
    '''
    #calculamos el exponencial
    exponencial = numero1**numero2
    #retornamos el resultado
    return exponencial
    
if __name__ == '__main__':
    numero1,numero2=leer_variables()
    #imprimo el exponencial
    print(numero1," elevado a ",numero2," es: ",calcular_exponencial_de_cualquier_numero(numero1,numero2))