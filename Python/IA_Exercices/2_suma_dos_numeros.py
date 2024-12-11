#Crea un programa que pida al usuario dos números y muestre la suma de ambos.

#Solucion común
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
suma = numero1 + numero2
print(f"La suma es: {suma}")

#Solucion optima
try:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    suma = numero1 + numero2
    print(f"La suma es: {suma}")
except ValueError:
    print("Por favor, ingresa solo valores numericos")