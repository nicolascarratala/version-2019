# Juan I. Martinez, Número de legajo 57018


def roman_to_decimal(roman_number):
    decimal_number = 0
    for letter in roman_number:
        if letter == "I":
            decimal_number += 1
        elif letter == "V":
            decimal_number += 5
        elif letter == "X":
            decimal_number += 10
        elif letter == "L":
            decimal_number += 50
        elif letter == "C":
            decimal_number += 100
        elif letter == "D":
            decimal_number += 500
        elif letter == "M":
            decimal_number += 1000
        
    return decimal_number



