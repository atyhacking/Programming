# Escribe un programa que cuente el número de palabras en una cadena de texto ingresada por el usuario.

espacio = True
palabra = 0
frase = input("Introduce una frase: ")

# Comprobamos si la frase está vacía o solo tiene espacios
if frase.strip() == "":
    print("La frase no tiene palabras.")
else:
    for letra in frase:
        if letra == " ":
            espacio = True  # Establecemos espacio en True cuando encontramos un espacio
        else:
            if espacio:  # Es lo mismo que poner "if espacio == True"
                palabra += 1  
                espacio = False  
    # Verificamos si hay palabras contadas
    if palabra > 0:
        print(f"La frase tiene {palabra} palabras.")
    else:
        print("La frase no tiene palabras.")

#El chat me ha ayudado un poco xD