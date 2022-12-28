import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        base : float
        altura : float
    '''
    #inicializo la variable base a cero
    base = 0
    #solicito al usuario que ingrese la variable numero1
    print("Ingrese el valor de la base del triangulo: ",end="")
    base = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(base<0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        base = validar_numeros_flotantes()
    #inicializo la variable altura a cero
    altura = 0
    #solicito al usuario que ingrese la variable altura
    print("Ingrese el valor de la altura del triangulo: ",end="")
    altura = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(altura<0):
        print("No ingrese numeros negativos, intente de nuevo: ",end="")
        altura = validar_numeros_flotantes()
    #retornamos la o las variables
    return base,altura
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

def calcular_area_del_triangulo(base,altura):
    '''
    Funcion que calcula el area de un triangulo

    Parametros:
    ------------
        base :float
        altura :float

    Retorna:
    ------------
        area : float
    '''
    #calculamos area del triangulo
    area = (base*altura)/2
    #retornamos area del triangulo
    return area
    
if __name__ == '__main__':
    #leo variables
    base,altura=leer_variables()
    #imprimo el area del triangulo
    print("El area del triangulo es: ",calcular_area_del_triangulo(base,altura))