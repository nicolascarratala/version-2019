def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = 0
    for letter in roman_number:
        

        if letter == "I":
            decimal_number += 1
            n = 1
        if letter == "V":
            decimal_number += 5
            n = 5
        if letter == "X":
            decimal_number += 10
            n = 10
        if letter == "C":
            decimal_number += 100
            n = 100
        if letter == "D":
            decimal_number += 500
            n = 500
        if n > ant:
            decimal_number -= ant*2




        ant = n
    print (decimal_number)
    return decimal_number
