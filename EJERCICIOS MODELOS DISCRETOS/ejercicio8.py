import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        libras : float
    '''
    #inicializo la variable radio a cero
    libras = 0
    #solicito al usuario que ingrese la variable radio
    print("Ingrese el valor en libras: ",end="")
    libras = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(libras<=0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        libras = validar_numeros_flotantes()
    #retornamos la o las variables
    return libras
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

def traformar_libras_a_kilos(libras):
    '''
    Funcion que transforma libras a kilogramos

    Parametros:
    ------------
        libras : float

    Retorna:
    ------------
        kilogramos : float
    '''
    #hacemos transformacion libras a kilogramos
    kilogramos = libras/2.205
    #retornamos la variable kilogramos
    return kilogramos

def traformar_libras_a_gramos(libras):
    '''
    Funcion que transforma libras a gramos

    Parametros:
    ------------
        libras : float

    Retorna:
    ------------
        gramos : float
    '''
    #hacemos transformacion libras a kilogramos
    gramos = libras*453.6
    #retornamos la variable kilogramos
    return gramos
if __name__ == '__main__':
    libras=leer_variables()
    #imprimimos la transformacion de libras a kilos y gramos
    print("Libras a kilogramos: ",traformar_libras_a_kilos(libras))
    print("Libras a gramos: ",traformar_libras_a_gramos(libras))