import os
import sys
import subprocess 
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

def imprimir_menu():
    '''
    Funcion que imprime el menu de opciones

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        No retorna ningun tipo de dato
    '''
    #Imprime en color amarillo
    print(chr(27)+"[1;33m"+"MENU") 
    #Imprime en color cian
    print("\033[;36m")
    print("███████████████████████████████████████████████████████████████████")
    print("█1. Numero de horas trabajadas y el coste por hora                █")
    print("█2. Calcular area y perimetro de un rectangulo                    █")
    print("█3. Calcular el arista lateral de una piramide                    █")
    print("█4. Calcular y=(x^z)/2                                            █")
    print("█5. Hallar el area de un trapezoide                               █")
    print("█6. Calcular el area de un cilindro                               █")
    print("█7. Calcular el area de un circulo                                █")
    print("█8. Transformar libras a kilos y gramos                           █")
    print("█9. Calcular (a+b^2)/2.5                                          █")
    print("█10. Calcular la formula de la velocidad                          █")
    print("█11. Centimetros a metros y kilometros                            █")
    print("█12. Realizar todas las operaciones aritmeticas con dos variables █")
    print("█13. Hallar la potencia de cualquier numero                       █")
    print("█14. Hallar la raiz cuadrada de cualquier numero                  █")
    print("█15. Hallar el area de un triangulo                               █")
    print("█16. Calcular y= x^2 + z^2                                        █")
    print("█17. Calcular el area de un paralelogramo                         █")
    print("█18. Pedir el nombre al usuario y saludarlo                       █")
    print("█19. Resolver  y= (-b+sqrt(b^2 + c))/2a                           █")
    print("█20. Calcular volumen de una esfera                               █")
    print("█21. Salir                                                        █")
    print("███████████████████████████████████████████████████████████████████")

if __name__ == '__main__':
    while True:
        os.system("cls")
        #imprime el menu de opciones
        imprimir_menu()
        #elejimos una opcion del menu
        print("Elija una opcion: ",end="")
        opcion=validar_numeros_enteros()
        while (opcion<1 or opcion>21):
            print("Elija una opcion dentro del rango:",end="")
            opcion=validar_numeros_enteros()
        if(opcion==1):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio1.py
            subprocess.call(["python", "./ejercicio1.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==2):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio2.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==3):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio3.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==4):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio4.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==5):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio5.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==6):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio6.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==7):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio7.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==8):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio8.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==9):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio9.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==10):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio10.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==11):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio11.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==12):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio12.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==13):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio13.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==14):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio14.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==15):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio15.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==16):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio16.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==17):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio17.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==18):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio18.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==19):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio19.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==20):
            #Pinta el texto en color morado
            print("\033[;35m")
            #Llamamos al archivo ejercicio2.py
            subprocess.call(["python", "./ejercicio20.py"])
            #pausamos el codigo
            os.system("pause")
        if(opcion==21):
            sys.exit()