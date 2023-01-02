import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        x1 : float
        x2 : float
        y1 : float
        y2 : float
    '''
    #inicializo la variable x1 a cero
    x1 = 0
    #inicializo la variable x2 a cero
    x2 = 0
    #inicializo la variable y1 a cero
    y1 = 0
    #inicializo la variable y2 a cero
    y2 = 0
    
    #solicito al usuario que ingrese la variable x1
    print("Ingrese el valor de la variable X1: ",end="")
    x1 = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable x
    print("Ingrese el valor de la variable X2: ",end="")
    x2 = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable y1
    print("Ingrese el valor de la variable y1: ",end="")
    y1 = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable x
    print("Ingrese el valor de la variable y2: ",end="")
    y2 = validar_numeros_flotantes()
    #retornamos la o las variables
    return x1,x2,y1,y2
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

def calcular_ecuacion_de_la_recta(x1,x2,y1,y2):
    '''
    Funcion que resuelve la ecuacion de la recta

    Parametros:
    ------------
        x1 : float
        x2 : float
        y1 : float
        y2 : float

    Retorna:
    ------------
        m : float
        b : float
    '''
    #resuelvo la ecuacion de la recta
    #primero calculo la pendiente
    m = (y2 - y1) / (x2 - x1)
    #luego calculo el termino independiente
    b = y1 - m * x1
    #retorno el resultado
    return m,b
if __name__ == '__main__':
    #leo variables
    x1,x2,y1,y2=leer_variables()
    #doy valores a la pendiente y termino independiente
    pendiente,termino_independiente = calcular_ecuacion_de_la_recta(x1,x2,y1,y2)
    #imprimo el resultado de la ecuacion
    print("La ecuacion de la recta es: y=",pendiente,"x+",termino_independiente)