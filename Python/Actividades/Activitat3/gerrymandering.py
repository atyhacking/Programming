def main():
    print("This program allows you to search through data about congressional voting districts")
    print("and determine whether a particular state is gerrymandered.")
    
    nombreEstado = input("Which state do you want to look up? ").strip()
    archivoDistritos = "districts.txt"
    archivoVotantes = "eligible_voters.txt"

    datosDistritos = leerArchivo(archivoDistritos)
    distritosEstado = encontrarDatosEstado(nombreEstado, datosDistritos)
    
    if not distritosEstado:
        print(f'"{nombreEstado}" not found.')
        return
    
    datosVotantes = leerArchivo(archivoVotantes)
    votantesEstado = encontrarDatosEstado(nombreEstado, datosVotantes)

    if not votantesEstado:
        print(f'Eligible voters data for "{nombreEstado}" not found.')
        return
    
    votosPerdidosDem, votosPerdidosRep, votosTotales = calcularVotosPerdidos(distritosEstado)
    votantesElegibles = int(votantesEstado.split(",")[1])
    
    print(f"Total Wasted Democratic votes: {votosPerdidosDem}")
    print(f"Total Wasted Republican votes: {votosPerdidosRep}")
    print(f"{votantesElegibles} eligible voters")
    
    ventaja = determinarGerrymandering(votosPerdidosDem, votosPerdidosRep, votosTotales)
    if ventaja:
        print(f"The {ventaja} have gained an advantage from gerrymandering in {nombreEstado}.")
    else:
        print(f"There is no significant gerrymandering in {nombreEstado}.")

def leerArchivo(nombreArchivo):
    with open(nombreArchivo, "r") as archivo:
        return archivo.readlines()

def encontrarDatosEstado(nombreEstado, lineasDatos):
    nombreEstadoMinuscula = nombreEstado.lower()
    for linea in lineasDatos:
        if linea.split(",")[0].strip().lower() == nombreEstadoMinuscula:
            return linea.strip()
    return None

def calcularVotosPerdidos(datosEstado):
    datos = datosEstado.split(",")[1:]
    votosPerdidosDem, votosPerdidosRep, votosTotales = 0, 0, 0
    
    for i in range(0, len(datos), 3):
        votosDem = int(datos[i + 1])
        votosRep = int(datos[i + 2])
        votosTotalesDistrito = votosDem + votosRep
        votosTotales += votosTotalesDistrito

        votosGanadores = (votosTotalesDistrito // 2) + 1
        if votosDem > votosRep:
            votosPerdidosDem += votosDem - votosGanadores
            votosPerdidosRep += votosRep
        else:
            votosPerdidosRep += votosRep - votosGanadores
            votosPerdidosDem += votosDem

    return votosPerdidosDem, votosPerdidosRep, votosTotales

def determinarGerrymandering(votosPerdidosDem, votosPerdidosRep, votosTotales):
    diferencia = abs(votosPerdidosDem - votosPerdidosRep)
    porcentaje = (diferencia / votosTotales) * 100

    if porcentaje >= 7:
        return "Democrats" if votosPerdidosDem > votosPerdidosRep else "Republicans"
    return None

if __name__ == "__main__":
    main()
