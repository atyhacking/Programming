#Escribe un programa que cuente el número de vocales en una cadena de texto proporcionada por el usuario.

try:
    contador = 0
    vocal = ["a", "e", "i", "o", "u"]
    texto = str(input("Ingresa una palabra o frase: ")).lower() #Para que tambien cuente si se introduce en mayuscula
    for letra in texto:
        if letra in vocal:
            contador += 1
    if contador == 0:
        print("Tu texto no tiene vocales")
    else:
        print(f"Tu texto tiene {contador} vocales")
except ValueError:
    print("Por favor, solo introduce texto")

