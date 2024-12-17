letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
try:
    numero = int(input("Introduce los numeros de tu DNI: "))
    if numero > 99999999 or numero <= 0:
        print("Introduce un valor valido")
    else:
        print(f"Tu letra del DNI es: {letras[numero%23]}")
except ValueError:
    print("Introduce solo valores numericos")