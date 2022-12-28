import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        x : float
        z : float
    '''
    #inicializo la variable x a cero
    x = 0
    #inicializo la variable z a cero
    z = 0
    #solicito al usuario que ingrese la variable x
    print("Ingrese el valor de la variable X: ",end="")
    x = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable z
    print("Ingrese el valor de la variable z: ",end="")
    z = validar_numeros_flotantes()
    #retornamos la o las variables
    return x,z
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

def calcular_ecuacion(x,z):
    '''
    Funcion que resuelve la ecuacion y= x^2 + z^2 

    Parametros:
    ------------
        x : int
        z : int

    Retorna:
    ------------
        y : int
    '''
    #resuelvo la ecuacion
    y = (x**2)+(z**2)
    #retorno el resultado
    return y
if __name__ == '__main__':
    #leo variables
    x,z=leer_variables()
    #imprio¿mo el resultado de la ecuacion
    print("La ecuacion y= x^2 + z^2 es: ",calcular_ecuacion(x,z))