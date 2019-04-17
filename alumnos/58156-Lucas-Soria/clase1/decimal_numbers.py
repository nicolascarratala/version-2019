def decimal_to_roman(decimal_number):

    r_dec = ''
    r_uni = ''
    r_udm = ''
    r_cent = ''
    roman_number = ''
    decimal_string = str(decimal_number) [::-1]
    nd = len(decimal_string)
    numero = 0
        
    #Unidad#
    numero = int(decimal_string [0])
    if (numero != 4 or numero != 9):
        while (numero > 0):
            if (numero >= 5):
                r_uni += "V"
                numero -= 5
            else:    
                r_uni += "I"
                numero -= 1
    if decimal_string[0] == '4':
        r_uni = 'IV'
    if decimal_string[0] == '9':
        r_uni = 'IX'

    #Decenas#
    if nd >= 2:
        numero = int(decimal_string [1])
        if (numero != 4 or numero != 9):
            while (numero > 0):
                if (numero >= 5):
                    r_dec += "L"
                    numero -= 5
                else:    
                    r_dec += "X"
                    numero -= 1
        if decimal_string[1] == '4' :
            r_dec = 'XL'
        if decimal_string[1] == '9' :
            r_dec = 'XC'

    #Centenas#
    if nd >= 3:
        numero = int(decimal_string [2])
        if (numero != 4 or numero != 9):
            while (numero > 0):
                if (numero >= 5):
                    r_cent += "D"
                    numero -= 5
                else:    
                    r_cent += "C"
                    numero -= 1
        if decimal_string[2] == '4':
            r_cent = 'CD'
        if decimal_string[2] == '9':
            r_cent = 'CM'

    #Unidades de mil#
    if nd >= 4:
        numero = int(decimal_string [3])
        if (numero < 4):
            while (numero > 0):
                r_udm += "M"
                numero -= 1
        else: 
            #Numeros mayores 3999, no estan contemplados en los numeros romanos
            nd = 5  
    if nd >= 5:
        roman_number = 'NumberOutOfLimit'
    else:
        roman_number = r_udm + r_cent + r_dec + r_uni
      
    return (roman_number)