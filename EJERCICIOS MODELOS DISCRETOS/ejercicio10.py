import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        distancia : float
        tiempo : float
    '''
    #inicializo la variable distancia
    distancia = 0
    #inicializo la variable altura a cero
    tiempo = 0
    #solicito al usuario que ingrese la variable radio
    print("Ingrese el valor de la distancia: ",end="")
    distancia = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(distancia<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        distancia = validar_numeros_flotantes()

    #solicito al usuario que ingrese la variable altura
    print("Ingrese el valor del tiempo: ",end="")
    tiempo = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(tiempo<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        tiempo = validar_numeros_flotantes()
    #retornamos la o las variables
    return distancia,tiempo
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
def formula_de_la_velocidad(distancia,tiempo):
    '''
    Funcion que calcula la velocidad con la ayuda de la fomula vel=dist/tiempo

    Parametros:
    ------------
        distancia : float
        tiempo : float

    Retorna:
    ------------
        velocidad : float
    '''
    velocidad=distancia/tiempo
    return velocidad

if __name__ == '__main__':
    distancia,tiempo=leer_variables()
    print("La velocidad es: ",formula_de_la_velocidad(distancia,tiempo)," m/s")