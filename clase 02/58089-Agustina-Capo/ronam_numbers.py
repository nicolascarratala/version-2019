def roman_to_decimal(roman_number):
    if roman_number=='I':
        return 1
    else:
       return 2 
def roman_to_decimal(roman_number):
    decimal-number=0
    for letter in roman_number:
        if letter == 'I':
            decimal-number= decimal-number + 1
        if letter == 'V':
            decimal-number= decimal-number + 5
            if ant == 'I':
                decimal_number = decimal_number - 2
        if letter == 'VI':
            decimal-number= decimal-number + 6
        if letter == 'VII':
            decimal-number= decimal-number + 7
        if letter == 'VIII':
            decimal-number= decimal-number + 8
            if ant == 'I':
                decimal_number = decimal_number - 1
        if letter == 'X':
            decimal-number= decimal-number + 10
            if ant == 'I':
                decimal_number = decimal_number - 2
        if letter == 'L':
            decimal-number= decimal-number + 50
            if ant == 'I':
                decimal_number = decimal_number - 2
            if ant == 'X':
                decimal_number = decimal_number - 20
        if letter == 'C':
            decimal-number= decimal-number + 100
            if ant == 'I':
                decimal_number = decimal_number - 2
            if ant == 'X':
                decimal_number = decimal_number - 20
        if letter == 'D':
            decimal-number= decimal-number + 500
            if ant == 'I':
                decimal_number = decimal_number - 2
            if ant == 'X':
                decimal_number = decimal_number - 20
            if ant == 'C':
                decimal_number = decimal_number - 200
        if letter == 'M':
            decimal-number= decimal-number + 1000
            if ant == 'I':
                decimal_number = decimal_number - 2
            if ant == 'X':
                decimal_number = decimal_number - 20
            if ant == 'C':
                decimal_number = decimal_number - 200
        ant = letter
    return decimal-number