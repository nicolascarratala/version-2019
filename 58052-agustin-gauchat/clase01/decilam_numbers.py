def decimal_to_roman(decimal_number):
    
    roman_number = ""
    
    #CALCULA DE MODULO Y CORRE LA COMA

    unidad = int(decimal_number%10)
    decimal_number = decimal_number/10
    decena = int(decimal_number%10)
    decimal_number = decimal_number/10
    centena = int(decimal_number%10)
    mil = int(decimal_number/10)


    #MILES

    if mil == 1:
        roman_number = roman_number + "M"

    if mil == 2:
        roman_number = roman_number + "MM"

    if mil == 3:
        roman_number = roman_number + "MMM"

    #CENTENAS

    if centena == 1:
        roman_number = roman_number + "C"

    if centena == 2:
        roman_number = roman_number + "CC"

    if centena == 3:
        roman_number = roman_number + "CCC"

    if centena == 4:
        roman_number = roman_number + "CD"

    if centena == 5:
        roman_number = roman_number + "D"
    
    if centena == 6:
        roman_number = roman_number + "DC"

    if centena == 7:
        roman_number = roman_number + "DCC"

    if centena == 8:
        roman_number = roman_number + "DCCC"

    if centena == 9:
        roman_number = roman_number + "CM"

    #DECENAS

    if decena == 1:
        roman_number = roman_number + "X"

    if decena == 2:
        roman_number = roman_number + "XX"

    if decena == 3:
        roman_number = roman_number + "XXX"

    if decena == 4:
        roman_number = roman_number + "XL"

    if decena == 5:
        roman_number = roman_number + "L"
    
    if decena == 6:
        roman_number = roman_number + "LX"

    if decena == 7:
        roman_number = roman_number + "LXX"

    if decena == 8:
        roman_number = roman_number + "LXXX"

    if decena == 9:
        roman_number = roman_number + "XC"

    #UNIDADES

    if unidad == 1:
        roman_number = roman_number + "I"

    if unidad == 2:
        roman_number = roman_number + "II"

    if unidad == 3:
        roman_number = roman_number + "III"

    if unidad == 4:
        roman_number = roman_number + "IV"

    if unidad == 5:
        roman_number = roman_number + "V"
    
    if unidad == 6:
        roman_number = roman_number + "VI"

    if unidad == 7:
        roman_number = roman_number + "VII"

    if unidad == 8:
        roman_number = roman_number + "VIII"

    if unidad == 9:
        roman_number = roman_number + "IX"

    



    return roman_number