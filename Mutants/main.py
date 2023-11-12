def ingresarDatos():
    dna = list()

    while(True):       
        while(True):

            cadena = input("Ingrese 6 caracteres, unicamente 'A,T,C,G' son validos: ").upper()

            if (validarCadena(cadena)):
                break
            else:
                print(f"La secuencia '{cadena}' no cumple con los requisitos!")
        
        dna.append(cadena)

        if (len(dna) == 6):
            break
    
    return dna

def validarCadena(cadena:str):
    if (len(cadena) != 6):
        return False
    
    for caracter in cadena:
        if (caracter != "A" and caracter != "T" and caracter != "C" and caracter != "G"):
            return False
    
    return True

def isMutant(dna:list):
    
    secuenciasEncontradas = 0

    secuenciasEncontradas += verificarFilas(dna)

    if (secuenciasEncontradas >= 2):
        return True

    secuenciasEncontradas += verificarColumnas(dna)

    if (secuenciasEncontradas >= 2):
        return True
    
    return False
    

    
    
            
def verificarFilas(dna:list):
    
    secuenciasEncontradas = 0

    for i in range(0,len(dna), 1):
        for j in range(0,int(len(dna)/2), 1):
            if (dna[i][j] == dna[i][j+3]):
                if dna[i][j] == dna[i][j+1] == dna[i][j+2]:
                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            break
    
    return secuenciasEncontradas

def verificarColumnas(dna:list):

    secuenciasEncontradas = 0

    for j in range(0,len(dna), 1):
        for i in range(0,int(len(dna)/2), 1):
            if (dna[i][j] == dna[i+3][j]):
                if dna[i][j] == dna[i+1][j] == dna[i+2][j]:
                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            break
    
    return secuenciasEncontradas



#dna = ingresarDatos()

dna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

if (isMutant(dna)):
    print(f"La secuencia corresponde a un MUTANTE!")
else:
    print(f"La secuencia NO corresponde a un mutante")