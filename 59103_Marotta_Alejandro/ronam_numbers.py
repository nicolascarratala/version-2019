def roman_to_decimal(roman_number):
    decimal_number_1= 0
    ant = ''

    for letter in roman_number:
        if letter == 'I':
            decimal_number_1 += 1
        if letter == 'V':
            if ant == 'I':
                decimal_number_1 -=2
            decimal_number_1 +=5
        if letter == 'X':
            if ant == 'I':
                decimal_number_1 -=2
            decimal_number_1 +=10
        if letter == 'L':
            if ant == 'X':
                decimal_number_1 -=20
            decimal_number_1 +=50
        if letter == 'C':
            if ant == 'X':
                decimal_number_1 -=20
            decimal_number_1 +=100
        if letter == 'D':
            if ant == 'C':
                decimal_number_1 -=200
            decimal_number_1 +=500
        if letter == 'M':
            if ant == 'C':
                decimal_number_1 -=200
            decimal_number_1 +=1000
        
        ant = letter
    return decimal_number_1

