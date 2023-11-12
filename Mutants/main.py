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

    print("Analizando Filas...")

    secuenciasEncontradas = verificarFilas(dna, secuenciasEncontradas)

    print(f"Secuencias encontradas en total: {secuenciasEncontradas}")

    if (secuenciasEncontradas >= 2):
        return True

    print("Analizando Columnas...")

    secuenciasEncontradas = verificarColumnas(dna, secuenciasEncontradas)

    print(f"Secuencias encontradas en total: {secuenciasEncontradas}")

    if (secuenciasEncontradas >= 2):
        return True

    print("Analizando Diagonales...")
    
    secuenciasEncontradas = verificarDiagonales(dna, secuenciasEncontradas)

    print(f"Secuencias encontradas en total: {secuenciasEncontradas}")

    if (secuenciasEncontradas >= 2):
        return True

    print("Analizando Diagonales Inversas...")
    
    secuenciasEncontradas = verificarDiagonalesInversas(dna, secuenciasEncontradas)

    print(f"Secuencias encontradas en total: {secuenciasEncontradas}")

    print("--------------------RESULTADO----------------------")

    if (secuenciasEncontradas >= 2):
        return True
    
    return False
    

    
    
            
def verificarFilas(dna:list, secuenciasEncontradas):

    for i in range(0,len(dna), 1):
        for j in range(0,int(len(dna)/2), 1):

            if (dna[i][j] == dna[i][j+3]):
                if dna[i][j] == dna[i][j+1] == dna[i][j+2]:

                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            return secuenciasEncontradas
    
    return secuenciasEncontradas

def verificarColumnas(dna:list, secuenciasEncontradas):

    for j in range(0,len(dna), 1):
        for i in range(0,int(len(dna)/2), 1):

            if (dna[i][j] == dna[i+3][j]):
                if dna[i][j] == dna[i+1][j] == dna[i+2][j]:

                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            return secuenciasEncontradas
    
    return secuenciasEncontradas

def verificarDiagonales(dna:list, secuenciasEncontradas):

    for i in range(int(len(dna)/2)):
        for j in range(int((len(dna)/2)-i)):

            if (dna[i+j][j] == dna[i+j+3][j+3]):
                if (dna[i+j][j] == dna[i+j+1][j+1] == dna[i+j+2][j+2]):
                    
                    secuenciasEncontradas += 1
                    break

        if secuenciasEncontradas >= 2:
            return secuenciasEncontradas
    
    for i in range(1, int(len(dna)/2)):
        for j in range(int(len(dna)/2)-i):

            if (dna[j][i+j] == dna[j+3][i+j+3]):
                if (dna[j][i+j] == dna[j+1][i+j+1] == dna[j+2][j+i+2]):

                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            return secuenciasEncontradas


    return secuenciasEncontradas

def verificarDiagonalesInversas(dna:list, secuenciasEncontradas):

    for i in range(int(len(dna)/2)):
        for j in range(int(len(dna))-1, (int(len(dna)/2)+1)-i, -1):

            if (dna[i][j] == dna[i+3][j-3]):
                if (dna[i][j] == dna[i+1][j-1] == dna[i+2][j-2]):

                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            return secuenciasEncontradas
    
    for i in range(int(len(dna)-2), int(len(dna)/2)-1 , -1):
        for j in range(i-2):

            if (dna[j][i-j] == dna[j+3][i-j-3]):
                if (dna[j][i-j] == dna[j+1][i-j-1] == dna[j+2][i-j-2]):
                    
                    secuenciasEncontradas += 1
                    break
        
        if secuenciasEncontradas >= 2:
            return secuenciasEncontradas
    
    return secuenciasEncontradas


dna = ingresarDatos()

if (isMutant(dna)):
    print(f"La secuencia corresponde a un MUTANTE!")
else:
    print(f"La secuencia NO corresponde a un mutante")