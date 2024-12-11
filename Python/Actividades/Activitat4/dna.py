def procesarSecuencia(secuencia):
    secuencia = secuencia.replace("-", "").replace(" ", "").upper()
    nucleotidos = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in secuencia:
        if nuc in nucleotidos:
            nucleotidos[nuc] += 1
    totalNucleotidos = len(secuencia)
    porcentajeNucleotidos = {nuc: (count / totalNucleotidos) * 100 for nuc, count in nucleotidos.items()}
    codones = [secuencia[i:i+3] for i in range(0, len(secuencia), 3)]
    esGen = False
    if secuencia.startswith("ATG") and any(secuencia.endswith(codon) for codon in ["TAA", "TAG", "TGA"]):
        if len(codones) >= 5:
            cgPercent = (nucleotidos["C"] + nucleotidos["G"]) / totalNucleotidos * 100
            if cgPercent >= 30:
                esGen = True
    return nucleotidos, porcentajeNucleotidos, codones, esGen

def procesarFichero(nombreFichero):
    with open(nombreFichero, 'r') as archivo:
        lineas = archivo.readlines()
    proteinas = []
    for i in range(0, len(lineas), 2):
        nombre = lineas[i].strip()
        secuencia = lineas[i+1].strip()
        nucleotidos, porcentajeNucleotidos, codones, esGen = procesarSecuencia(secuencia)
        proteinas.append({
            "nombre": nombre,
            "nucleotidos": nucleotidos,
            "porcentajeNucleotidos": porcentajeNucleotidos,
            "codones": codones,
            "esGen": esGen
        })
    return proteinas

proteinasDna = procesarFichero("dna.txt")
proteinasEcoli = procesarFichero("ecoli.txt")

for proteina in proteinasDna + proteinasEcoli:
    print(f"Proteína: {proteina['nombre']}")
    print(f"Nucleótidos: {proteina['nucleotidos']}")
    print(f"Porcentajes de nucleótidos: {proteina['porcentajeNucleotidos']}")
    print(f"Codones: {proteina['codones'][:10]}...")
    print(f"Es un gen: {'Sí' if proteina['esGen'] else 'No'}\n")
