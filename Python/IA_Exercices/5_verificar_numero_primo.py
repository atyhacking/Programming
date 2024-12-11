#Crea un programa que verifique si un número dado por el usuario es primo.

import math
def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

try:
    numero = int(input("Ingresa un número: "))
    if es_primo(numero):
        print(f"{numero} es un número primo!")
    else:
        print(f"{numero} no es un número primo!")
except ValueError:
    print("Por favor, introduce solo números enteros.")

#Hecho con chat, se me complico xD
