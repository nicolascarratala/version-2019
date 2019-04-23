def cifrador(secreto, clave):
    resultado = ""
    resultadolista = []
    lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    movimientos = []
    clavelarga = []
    conteo = 0
    x = 0
    y = 0
    z = 0
    while len(clavelarga) < len(secreto):
        clavelarga.append(clave[conteo])
        conteo = conteo + 1
        if conteo > len(clave)-1:
            conteo = 0

    for letter in clavelarga:
        movimientos.append(lista.index(letter))
    
    conteo = 0
    for letter in secreto:
        x = lista.index(letter)
        y = movimientos[conteo]
        z = x + y
        if z > len(lista):
            z = z - len(lista)
        
        resultadolista.append(lista[z])
        conteo = conteo + 1

    resultado = "".join(resultadolista)
    return resultado

        

        
