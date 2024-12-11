#Crea una función que calcule el factorial de un número proporcionado por el usuario.

def calcular_factorial(a):
    factorial = 1
    for b in range(1, a + 1):
        factorial *= b
    return factorial

try:
    numero = int(input("Introduce un numero: "))
    print(f"El numero es: {calcular_factorial(numero)}")
except ValueError:
    print("Introduce solo valores numericos")