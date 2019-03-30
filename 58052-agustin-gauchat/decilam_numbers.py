def decimal_to_roman(decimal_number):
    
    roman_number = ""
    
    unidad = decimal_number%10
    decimal_number = decimal_number/10
    decena = decimal_number%10
    decimal_number = decimal_number/10
    centena = decimal_number%10
    mil = decimal_number/10

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