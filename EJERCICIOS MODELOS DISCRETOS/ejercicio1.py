import os
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        horasTrabajadas : float
        costoHora : float
    '''
    #inicializo la variable horasTrabajadas a cero
    horasTrabajadas = 0
    #inicializo la variable costoHora a cero
    costoHora = 0
    print("Ingrese el numero de horas trabajadas: ",end="")
    #solicito al usuario que ingrese el numero de horas trabajadas
    horasTrabajadas = validar_numeros_flotantes()
    #ciclo repetitivo que valida numeros negativos
    while(horasTrabajadas <= 0):
        print("No ingrese numeros negativos,ingrese de nuevo: ",end="")
        horasTrabajadas = validar_numeros_flotantes()
    #solicito al usuario que ingrese el costo que vale cada hora trabajada
    print("Ingrese el costo por hora: ",end="")
    costoHora = validar_numeros_flotantes()
    while(costoHora <= 0):
        print("No ingrese numeros negativos,ingrese de nuevo: ",end="")
        costoHora = validar_numeros_flotantes()
    
    #retornamos la o las variables
    return horasTrabajadas,costoHora
def validar_numeros_flotantes():
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
            numero=float(input())
            #rempemos ciclo repetitivo
            break
        except ValueError:
            print("No ha ingresado un numero ,ingrese de nuevo:",end="")
    return numero

def calcular_salario_por_horas_trabajadas(horasTrabajadas,costoHora):
    '''
    Funcion que calcula el salario con las variables de las horas trabajadas y el costo por hora

    Parametros:
    ------------
        horasTrabajadas : int
        costoHora : int

    Retorna:
    ------------
        salario : int
    '''
    salario=horasTrabajadas*costoHora
    return salario

if __name__ == '__main__':
    #leo variables
    horasTrabajadas,costoHora=leer_variables()
    #imprimo el salario
    print("Salario calculado: ",calcular_salario_por_horas_trabajadas(horasTrabajadas,costoHora)," dolares $$$")