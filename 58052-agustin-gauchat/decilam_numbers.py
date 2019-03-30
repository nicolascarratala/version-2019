def decimal_to_roman(decimal_number):
    
    roman_number = ""
    
    unidad = decimal_number%10
    decimal_number = decimal_number/10
    decena = decimal_number%10
    decimal_number = decimal_number/10
    centena = decimal_number%10
    mil = decimal_number/10

    if unidad == 1:
        roman_number = roman_number + "I"



    return roman_number