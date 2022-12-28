import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        base1 : float
        base2 : float
        altura : float
    '''
    #inicializo la variable base1 a cero
    base1 = 0
    #inicializo la variable base2 a cero
    base2 = 0
    #inicializo la variable altura a cero
    altura = 0
    #solicito al usuario que ingrese la variable base 1
    print("Ingrese el valor de base 1 del trapezoide: ",end="")
    base1 = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(base1<0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        base1 = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable base 2
    print("Ingrese el valor de base 2 del trapezoide: ",end="")
    base2 = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(base2<0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        base2 = validar_numeros_flotantes()
    #solicito al usuario que ingrese la variable altura
    print("Ingrese el valor de la altura del trapezoide: ",end="")
    altura = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(altura<0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        altura = validar_numeros_flotantes()
    #retornamos la o las variables
    return base1,base2,altura
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

def calcular_area_trapezoide(altura,base1,base2):
    '''
    Funcion que calcula el area de un trapezoide

    Parametros:
    ------------
        altura : float
        base1 : float
        base2 : float

    Retorna:
    ------------
        area : float
    '''
    #calculo el area del trapezoide con la formula area=1/2(h) * (b1+b2)
    area=((1/2)*altura)*(base1+base2)
    return area

if __name__ == '__main__':
    base1,base2,altura=leer_variables()
    print("El area del trapezoide es: ",calcular_area_trapezoide(altura,base1,base2)," unidades")