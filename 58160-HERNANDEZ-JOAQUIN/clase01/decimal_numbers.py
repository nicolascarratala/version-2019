def decimal_to_roman(decimal):
    
    unidad = ''
    dec = ''
    roman_number = ''
    decimal = str(decimal) [::-1]
    cantidad = len(decimal)
    

    if decimal[0] == '0':
        unidad = unidad + ''
    if decimal[0] == '1':
        unidad = unidad + 'I'
    if decimal[0] == '2':
        unidad = unidad + 'II'
    if decimal[0] == '3':
        unidad = unidad + 'III'
    if decimal[0] == '4':
        unidad = unidad + 'IV'
    if decimal[0] == '5':
        unidad = unidad + 'V'
    if decimal[0] == '6':
        unidad = unidad + 'VI'
    if decimal[0] == '7':
        unidad = unidad + 'VII'
    if decimal[0] == '8':
        unidad = unidad + 'VIII'
    if decimal[0] == '9':
        unidad = unidad + 'IX'

    if cantidad >= 2 :
        
        if decimal[1]=='0':
            dec = dec + ''
        
        if decimal[1]=='1':
            dec = dec + "X"

        if decimal[1]=='2':
            dec = dec + "XX"

        if decimal[1]=='3':
            dec = dec + "XXX"

        if decimal[1]=='4':
            dec = dec+ "XL"

        if decimal[1]=='5':
            dec = dec + "L"

        if decimal[1]=='6':
            dec = dec + "LX"
        
        if decimal[1]=='7':
            dec = dec + "LXX"
        
        if decimal[1]=='8':
            dec = dec + "LXXX"


    else:
        roman_number = dec+unidad
 
    return (roman_number)