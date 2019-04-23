def decimal_to_roman(decimal_number):
    x = str(decimal_number)
    z = len(x)
    y = 0
    q = ""
    a = []
    b = []
    resultado = ""
    lista = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX"
    }
    
    for num in x:

        y = lista[int(num)]
        if z == 4:
            for letra in y:
                if decimal_number < 4000:
                    if letra == "I":
                        
                        b.append("M")
                    else:
                        b.append(str(letra))
                else:
                    if decimal_number > 5999:
                        if letra == "I":
                            letra = "M"
                            b.append("M")
                        else:
                            b.append(str(letra))
                    else:
                        b.append(str(letra))
        if z == 3:
            for letra in y:
                if letra == "I":
                    letra = "C"
                    b.append("C")
                else:
                    if letra == "V":
                        letra = "D"
                        b.append("D")
                    else:
                        if letra == 'X':
                            letra = 'M'
                            b.append("M")
                        else:
                            b.append(str(letra))
        if z == 2:
            for letra in y:
                if letra == 'I':
                    letra = 'X'
                    b.append("X")
                else:
                    if letra == 'V':
                        letra = 'L'
                        b.append("L")
                    else:
                        if letra == 'X':
                            letra = 'C'
                            b.append("C")
                        else:
                            b.append(str(letra))
        if z == 1:
            for letra in y:
                b.append(str(letra)) 
        z = z -1
    q = ''.join(b)
    a.append(q)
    resultado = ''.join(a)
    return resultado

                    
                
            

    