#Crea una función que verifique si una cadena dada es un palíndromo 
#(se lee igual de izquierda a derecha que de derecha a izquierda).

#Solucion común
palabra_invertida = ""
palabra = input("Introduce la palabra a verificar: ")
for letra in palabra: 
    palabra_invertida = letra + palabra_invertida
if palabra_invertida.lower() == palabra.lower():
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


#Solucion optima
palabra2 = input("Introduce la palabra a verificar: ")
if palabra2.lower() == palabra2[::-1].lower():
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
