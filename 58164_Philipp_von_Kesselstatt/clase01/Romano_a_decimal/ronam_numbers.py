def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = 0
    for letter in roman_number:
        

        if letter == "I":
            n = 1
            decimal_number += n
        if letter == "V":
            n = 5
            decimal_number += n
        if letter == "X":
            n = 10
            decimal_number += n
        if letter == "L":
            n = 50
            decimal_number += n
        if letter == "C":
            n = 100
            decimal_number += n
        if letter == "D":
            n = 500
            decimal_number += n
        if letter == "M":
            n = 1000
            decimal_number += n
        if n > ant:
            decimal_number -= ant*2

        ant = n
    print (decimal_number)
    return decimal_number
