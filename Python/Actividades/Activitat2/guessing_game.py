import random

MAX_NUMBER = 100

def jugar_un_joc():
    numeroRandom = random.randint(1, MAX_NUMBER)
    intents = 0
    encertat = False

    print(f"I'm thinking of a number between 1 and {MAX_NUMBER}...")

    while not encertat:
        try:
            advivinar = int(input("Your guess? "))
            intents += 1

            if advivinar < numeroRandom:
                print("It's higher.")
            elif advivinar > numeroRandom:
                print("It's lower.")
            else:
                encertat = True
                print(f"You got it right in {intents} guesses!")

        except ValueError:
            print("Please enter a valid number.")

    return intents

def mostrar_estadistiques(jocs, intents_total):
    if jocs == 0:
        return

    mitjana_intents = round(intents_total / jocs, 1)
    millor_joc = min(jocs, key=lambda x: x[0])[0]

    print("\nOverall results:")
    print(f"Total games   = {jocs}")
    print(f"Total guesses = {intents_total}")
    print(f"Guesses/game  = {mitjana_intents}")
    print(f"Best game     = {millor_joc}")

def main():
    jocs = []
    intents_total = 0
    jugar_de_nou = True

    while jugar_de_nou:
        intents_joc = jugar_un_joc()
        jocs.append(intents_joc)
        intents_total += intents_joc

        resposta = input("Do you want to play again? ")
        if resposta.lower().startswith('y'):
            jugar_de_nou = True
        else:
            jugar_de_nou = False

    mostrar_estadistiques(jocs, intents_total)

if __name__ == "__main__":
    main()
