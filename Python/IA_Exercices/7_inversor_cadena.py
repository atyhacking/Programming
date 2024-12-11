#Pide al usuario que ingrese una cadena y devuelve la cadena invertida.

invertido = ""    
cadena = input("Introduce una cadena de texto: ")
for char in cadena:
    invertido = char + invertido
print(f"{cadena} = {invertido}")


