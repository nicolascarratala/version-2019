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
        if letter == 'VI':
            decimal-number= decimal-number + 6
        if letter == 'VII':
            decimal-number= decimal-number + 7
        if letter == 'VIII':
            decimal-number= decimal-number + 8
        if letter == 'X':
            decimal-number= decimal-number + 10
    return decimal-number