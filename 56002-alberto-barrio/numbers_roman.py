def decimal_to_roman(decimal_number):
    roman_number=''
    ant=''
    for number in str(decimal_number):
        
        if number == '1':
            if ant == '1':
                roman_number='X'
            roman_number += 'I'
            
        if number == '2':
            roman_number += 'II'

        if number == '3':
            roman_number += 'III'
        
        if number == '4':
            roman_number += 'IV'

        if number == '5':
            roman_number += 'V'

        if number == '6':
            roman_number += 'VI'

        if number == '7':
            roman_number += 'VII'

        if number == '8':
            roman_number += 'VIII'

        if number == '9':
            roman_number += 'IX'
        
        if number == '0':
            roman_number = 'X'
        
        ant=str(number)
                
    
    return roman_number