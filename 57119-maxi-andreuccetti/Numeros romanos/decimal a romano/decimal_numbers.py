def decimal_to_roman(decimal):
    
    roman_number = ''
    num = 0

    
    decimal_number = str(decimal) [::-1]
    longitud = len(decimal_number) 
    
    
    u =''
    d =''
    c =''
    m =''

    
    num = int(decimal_number [0])
    
    if (num != 4 or num != 9):
        while (num > 0):
            if (num >= 5):
                u += "V"
                num -= 5
            else:    
                u += "I"
                num -= 1
    if decimal_number[0] == '4':
        u = 'IV'
    if decimal_number[0] == '9':
        u = 'IX'

    
    if longitud >= 2:
        num = int(decimal_number [1])
        if (num != 4 or num != 9):
            while (num > 0):
                if (num >= 5):
                    d += "L"
                    num -= 5
                else:    
                    d += "X"
                    num -= 1
        if decimal_number[1] == '4' :
            d = 'XL'
        if decimal_number[1] == '9' :
            d = 'XC'

    
    if longitud >= 3:
        num = int(decimal_number [2])
        if (num != 4 or num != 9):
            while (num > 0):
                if (num >= 5):
                    c += "D"
                    num -= 5
                else:    
                    c += "C"
                    num -= 1
        if decimal_number[2] == '4':
            c = 'CD'
        if decimal_number[2] == '9':
            c = 'CM'

   
    if longitud >= 4:
        num = int(decimal_number[3])
        if (num < 4):
            while (num > 0):
                m += "M"
                num -= 1
   
      
    roman_number = m + c + d + u
      
    return (roman_number)