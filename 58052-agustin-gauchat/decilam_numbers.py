def decimal_to_roman(decimal_number, decimal_numberr):
    romann_number = ""
    ant = ""
    for letter in decimal_number:
        if decimal_numberr < 9:
            if letter == '1':
                romann_number = romann_number + "I"

            if letter == '2':
                romann_number = romann_number + "II"
        
        ant = letter


    return romann_number