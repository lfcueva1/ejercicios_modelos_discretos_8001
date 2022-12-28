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
    #inicializo la variable centrimetro a cero
    centimetro = 0
    #solicito al usuario que ingrese la variable radio
    print("Ingrese el valor de la longitud en centimetro: ",end="")
    centimetro = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(centimetro<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        centimetro = validar_numeros_flotantes()
    #retornamos la o las variables
    return centimetro
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

def convertir_centimetro_a_metro(centimetro):
    '''
    Funcion que convierte centimetro a metro

    Parametros:
    ------------
        centimetro : float

    Retorna:
    ------------
        metro : float
    '''
    #convierto centimetro a metro
    metro = centimetro/100
    #retorno metro
    return metro

def convertir_centimetro_a_kilometro(centimetro):
    '''
    Funcion que convierte centimetro a kilometro

    Parametros:
    ------------
        centimetro : float

    Retorna:
    ------------
        kilometro : float
    '''
    #convierto centimetro a metro
    kilometro = centimetro/100000
    #retorno kilometro
    return kilometro

if __name__ == '__main__':
    
    centimetro = leer_variables()
    #imprimimos la conversion de (cm) a (m) y (km)
    print("Centimetro a metro es: ",convertir_centimetro_a_metro(centimetro))
    print("Centimetro a kilometro es: ",convertir_centimetro_a_kilometro(centimetro))