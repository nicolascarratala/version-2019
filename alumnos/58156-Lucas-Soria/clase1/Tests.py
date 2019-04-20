def decimal_to_roman(decimal_number):

    r_dec = ''
    r_uni = ''
    r_udm = ''
    r_cent = ''
    roman_number = ''
    decimal_string = str(decimal_number) [::-1]
    nd = len(decimal_string)
    numero = 0
    op = [r_uni, r_dec, r_cent, r_udm]
    num1 = ["V", "L", "D"]
    num2 = ["I", "X", "C", "M"]
    nume1 = ["IV", "XL", "CD"]
    nume2 = ["IX", "XC", "CM"]
    q = 0
        
    while q <= nd:
        numero = int(decimal_string [q])
        if (numero != 4 or numero != 9):
            while (numero > 0):
                if (numero >= 5):
                    op[q] += num1[q]
                    numero -= 5
                else:    
                    op[q] += num2[q]
                    numero -= 1
        if decimal_string[q] == '4':
            op[q] = nume1[q]
        if decimal_string[q] == '9':
            op[q] = nume2[q]

        q += 1

        if nd >= 4 and numero >= 4:
            #Numeros mayores 3999, no estan contemplados en los numeros romanos
            nd = 5 
        if nd >= 5:
            roman_number = 'NumberOutOfLimit'
        else:
            roman_number = r_udm + r_cent + r_dec + r_uni


 
      
    return (roman_number)