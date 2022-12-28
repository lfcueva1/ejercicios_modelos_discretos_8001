import os

def saludar_al_usuario(nombre):
    '''
    Funcion que saluda al usuario despues de haber ingresado su nombre

    Parametros:
    ------------
        nombre : str

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    print("Hola ",nombre," es un gusto conocerte")
if __name__ == '__main__':
    nombre=(input("Por favor, ingrese su nombre: "))
    saludar_al_usuario(nombre)