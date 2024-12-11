import random
#Crea un juego donde el usuario tiene que adivinar un número generado aleatoriamente entre 1 y 100. 
#El programa debe dar pistas si el número es mayor o menor que el número objetivo.

#Solucion común
def adivinanza(numero_random):
    numero_user = int(input("Introduce un numero del 1 al 100: "))
    try:
        if numero_user > 100 or numero_user < 1:
            print("El numero introducido no entra dentro del rango permitido.")
            adivinanza(numero_random)
        else:
            if numero_random == numero_user:
                print("Lo has logrado!")
                return 
            else:
                if numero_random > numero_user:
                    print("El numero introducido es demasiado pequeño")
                else:
                    print("El numero introducido es demasiado grande")
                adivinanza(numero_random)
    except ValueError:
        print("Por favor, introduce solo valores enteros")
        adivinanza(numero_random)
numero_random =  numero_random = random.randint(1, 100)
adivinanza(numero_random)


#Solucion óptima    
import random

def adivinanza():
    numero_random = random.randint(1, 100)
    while True:
        try:
            numero_user = int(input("Introduce un número del 1 al 100: "))
            if numero_user > 100 or numero_user < 1:
                print("El número introducido no entra dentro del rango permitido.")
            elif numero_user == numero_random:
                print("¡Lo has logrado!")
                break
            elif numero_user < numero_random:
                print("El número introducido es demasiado pequeño.")
            else:
                print("El número introducido es demasiado grande.")
        except ValueError:
            print("Por favor, introduce solo valores enteros.")
adivinanza()

