def roman_to_decimal(roman_number):

    decimal_number = 0
    aux = ""
    for letter in roman_number:
        if letter == "I":
            decimal_number += 1
        if letter == "V":
            if aux == "I":
                decimal_number -= 2
            decimal_number += 5
        if letter == "X":
            if aux == "I":
                decimal_number -= 2 
            decimal_number += 10
        if letter == "L":
            if aux == "X":
                decimal_number -=20 
            decimal_number +=50
        if letter == "C":
            if aux == "X":
                decimal_number -=20 
            decimal_number +=100
        if letter == "D":
            if aux == "C":
                decimal_number -=200
            decimal_number += 500
        if letter == "M":
            if aux == "C":
                decimal_number -=200 
            decimal_number +=1000
        aux = letter 
    return decimal_number
