def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = ''
    for x in roman_number:
        if x == 'I':
            decimal_number += 1
        if x == 'V':
            decimal_number += 5
            if ant == 'I':
                decimal_number -= 2
        if x == 'X':
            decimal_number += 10
            if ant == 'I':
                decimal_number -= 2
        if x == 'L':
            decimal_number += 50
            if ant == 'X':
                decimal_number -= 20
            if ant == 'I':
                decimal_number -= 2
        if x == 'C':
            decimal_number += 100
            if ant == 'L':
                decimal_number -= 100
            if ant == 'X':
                decimal_number -= 20
            if ant == 'I':
                decimal_number -= 2
        if x == 'D':
            decimal_number += 500
            if ant == 'C':
                decimal_number -= 200
            if ant == 'L':
                decimal_number -= 100
            if ant == 'X':
                decimal_number -= 20
            if ant == 'I':
                decimal_number -= 2
        if x == 'M':
            decimal_number += 1000
            if ant == 'D':
                decimal_number -= 1000
            if ant == 'C':
                decimal_number -= 200
            if ant == 'L':
                decimal_number -= 100
            if ant == 'X':
                decimal_number -= 20
            if ant == 'I':
                decimal_number -= 2
        ant = x
    return decimal_number

    # C 100
    # D 500
    # M 1000