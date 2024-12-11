#Pide al usuario un número e indica si es par o impar.

#Solucion comun
numero = int(input("Introduce un numero: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#Solucion optima
try:
    numero = int(input("Introduce un numero: "))
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Por favor, ingresa solo valores numericos")

