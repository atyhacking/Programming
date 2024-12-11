import random

NUMERO_MAXIMO = 100

def jugarUnJuego():
    numeroAleatorio = random.randint(1, NUMERO_MAXIMO)
    intentos = 0
    acertado = False

    print(f"I'm thinking of a number between 1 and {NUMERO_MAXIMO}...")

    while not acertado:
        try:
            adivinar = int(input("Your guess? "))
            intentos += 1

            if adivinar < numeroAleatorio:
                print("It's higher.")
            elif adivinar > numeroAleatorio:
                print("It's lower.")
            else:
                acertado = True
                print(f"You got it right in {intentos} guesses!")

        except ValueError:
            print("Please enter a valid number.")

    return intentos

def mostrarEstadisticas(juegos, intentosTotales):
    if juegos == 0:
        return

    promedioIntentos = round(intentosTotales / juegos, 1)
    mejorJuego = min(juegos, key=lambda x: x[0])[0]

    print("\nOverall results:")
    print(f"Total games   = {juegos}")
    print(f"Total guesses = {intentosTotales}")
    print(f"Guesses/game  = {promedioIntentos}")
    print(f"Best game     = {mejorJuego}")

def main():
    juegos = []
    intentosTotales = 0
    jugarDeNuevo = True

    while jugarDeNuevo:
        intentosJuego = jugarUnJuego()
        juegos.append(intentosJuego)
        intentosTotales += intentosJuego

        respuesta = input("Do you want to play again? ")
        if respuesta.lower().startswith('y'):
            jugarDeNuevo = True
        else:
            jugarDeNuevo = False

    mostrarEstadisticas(juegos, intentosTotales)

if __name__ == "__main__":
    main()
