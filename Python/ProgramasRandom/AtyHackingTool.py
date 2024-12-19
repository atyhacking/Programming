import subprocess
def cupp():
    subprocess.run("cupp -i", shell=True)

print("1.Wordlist Generator")
menuPrincipal = int(input("Elige una opcion: "))
if menuPrincipal == 1: 
    print("1.cupp")
    menuWordlistGenerator = input("Elige una opcion: ")
    if menuWordlistGenerator == 1:
        cupp()
        