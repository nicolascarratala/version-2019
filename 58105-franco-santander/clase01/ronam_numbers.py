def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = 0
    for letter in roman_number:
        if letter == 'I':
            decimal_number = decimal_number + 1
            pass
        pass
        if letter == 'V':
            decimal_number = decimal_number + 5
            if ant == 'I':
                decimal_number = decimal_number - 2
                pass
            pass
        pass
        if letter == 'X':
            decimal_number = decimal_number + 10
            if ant == 'I':
                decimal_number = decimal_number -2
                pass
            pass
        pass
        if letter == 'L':
            decimal_number = decimal_number + 50
            if ant == 'X':
                decimal_number = decimal_number - 20
                pass
            pass
        pass
        if letter == 'C':
            decimal_number = decimal_number + 100
            if ant == 'X':
                decimal_number = decimal_number - 20
                pass
            pass
        pass
        if letter == 'D':
            decimal_number = decimal_number + 500
            if ant == 'C':
                decimal_number = decimal_number - 200
                pass
            pass
        pass
        if letter == 'M':
            decimal_number = decimal_number + 1000
            if ant == 'C':
                decimal_number = decimal_number - 200
                pass
            pass
        pass
        ant = letter
    return decimal_number
def decimal_to_roman(decimal_number):
    roman_number = 1
    
    for number in decimal_number:
        if number == 1:
            roman_number = 'I'
            pass
        pass
    return roman_number
