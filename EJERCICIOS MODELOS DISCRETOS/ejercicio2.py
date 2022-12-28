import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        ancho : float
        longitud : float
    '''
    #inicializo la variable ancho a cero
    ancho = 0
    #inicializo la variable longitud a cero
    longitud = 0
    #solicito al usuario que ingrese el ancho de un rectangulo
    print("Ingrese el valor del ancho del rectangulo: ",end="")
    ancho = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(ancho<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        ancho = validar_numeros_flotantes()
    #solicito al usuario que ingrese el perimetro de un rectangulo
    print("Ingrese el valor de la longitud del rectangulo: ",end="")
    longitud = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(longitud<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        longitud = validar_numeros_flotantes()
    
    #retornamos la o las variables
    return ancho,longitud
def validar_numeros_flotantes():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero

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
def calcular_area_rectangulo(ancho,longitud):
    '''
    Funcion que calcula el area de un rectangulo

    Parametros:
    ------------
        ancho : float
        longitud : float

    Retorna:
    ------------
        area : float
    '''
    #calculo el area de un rectangulo
    area = ancho * longitud
    return area

def calcular_perimetro_rectangulo(ancho,longitud):
    '''
    Funcion que calcula el perimetro de un rectangulo

    Parametros:
    ------------
        ancho : float
        longitud : float

    Retorna:
    ------------
        perimetro : float
    '''
    #calculo el perimetro de un rectangulo
    perimetro = (2*ancho) + (2*longitud)
    return perimetro

if __name__ == '__main__':
    #leo variables
    ancho,longitud = leer_variables()
    #imprime el area y perimetro de un rectangulo
    print("El area del rectangulo es: ",calcular_area_rectangulo(ancho,longitud))
    print("El perimetro del rectangulo es: ",calcular_perimetro_rectangulo(ancho,longitud))