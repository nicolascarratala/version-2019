def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = ''
    for letter in roman_number:
        if letter == 'i':
            decimal_number += 1
        elif letter == 'v':
            decimal_number += 5
            if ant == 'i':
                decimal_number -= 2
        elif letter == 'x':
            decimal_number += 10
            if ant == 'i':
                decimal_number -= 2
        elif letter == 'l':
            decimal_number += 50
            if ant == 'x':
                decimal_number -= 20
        elif letter == 'c':
            decimal_number += 100
            if ant == 'x':
                decimal_number -= 20
        elif letter == 'd':
            decimal_number += 500
            if ant == 'c':
                decimal_number -= 200
        elif letter == 'm':
            decimal_number += 1000
            if ant == 'c':
                decimal_number -= 200
        ant = letter

    return decimal_number
