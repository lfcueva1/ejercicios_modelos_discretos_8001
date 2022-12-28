import os
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
    #inicializo la variable x a cero
    x = 0
    #inicializo la variable z a cero
    z = 0
    #solicito al usuario que ingrese la variable x
    print("Ingrese el valor de la variable X: ",end="")
    x = validar_numeros_enteros()

    #solicito al usuario que ingrese la variable z
    print("Ingrese el valor de la variable z: ",end="")
    z = validar_numeros_enteros()
    #retornamos la o las variables
    return x,z
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

def calcular_ecuacion(x,z):
    '''
    Funcion que resuelve la ecuacion

    Parametros:
    ------------
        x : int
        z : int

    Retorna:
    ------------
        y : float
    '''
    #imprime la ecuacion a resolver
    print("y=(x^z)/2")
    #resuelvo la ecuacion
    y=(x**z)/2
    #retorno la variable y
    return y

if __name__ == '__main__':
    x,z=leer_variables()
    #imprimo el resultado
    print("La ecuacion y=(x^z)/2 es: ",calcular_ecuacion(x,z))