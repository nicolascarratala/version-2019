def decimal_to_roman(decimal_number):
    romann_number = ""
    ant = ""
    
    for letter in decimal_number:
        if int(letter) < 9:
            if letter == '1':
                romann_number = romann_number + "I"

            if letter == '2':
                romann_number = romann_number + "II"
            
            if letter == '3':
                romann_number = romann_number + "III"
        
        ant = letter


    return romann_number