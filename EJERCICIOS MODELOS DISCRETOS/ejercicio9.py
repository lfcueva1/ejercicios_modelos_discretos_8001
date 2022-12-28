import os
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
    '''
    #inicializo la variable x a cero
    a = 0
    #inicializo la variable z a cero
    b = 0
    #solicito al usuario que ingrese la variable x
    print("Ingrese el valor de la variable a: ",end="")
    a = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable z
    print("Ingrese el valor de la variable b: ",end="")
    b = validar_numeros_flotantes()
    #retornamos la o las variables
    return a,b
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

def calcular_ecuacion(a,b):
    '''
    Funcion que resuelve la ecuacion

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        resultado : float
    '''
    print("(a+b^2)/2.5 ")
    #resolvemos la ecuacion
    resultado = (a+(b**2))/2.5
    #retornamos la variable resultado
    return resultado
if __name__ == '__main__':
    a,b=leer_variables()
    #imprime resultado de la ecuacion
    print("El resultado de la ecuacion es: ",calcular_ecuacion(a,b))