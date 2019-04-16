def roman_to_decimal(roman_number):
    """
    if roman_number == 'I':
        return 1
    elif roman_number == 'II':
        return 2
    elif roman_number == 'III':
        return 3
    """

    decimal_number = 0
    aux = ''
    for letter in roman_number:
        if letter == 'I':
            decimal_number += 1
        if letter == 'V':
            if aux == 'I':
                decimal_number -= 2
            decimal_number += 5
        if letter == 'X':
            if aux == 'I':
                decimal_number -= 2
            decimal_number += 10
        if letter == 'L':
            if aux == 'X':
                decimal_number -=20
            decimal_number += 50
        if letter == 'C':
            if aux == 'X':
                decimal_number -=20
            decimal_number += 100
        if letter == 'D':
            if aux == 'C':
                decimal_number -=200
            decimal_number +=500
        if letter == 'M':
            if aux == 'C':
                decimal_number -=200
            decimal_number +=1000
        aux = letter
    return decimal_number
