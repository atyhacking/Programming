#Escribe un programa que genere una lista de los cuadrados de los números del 1 al 10 y los imprima.

for numero in range(1, 11):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")