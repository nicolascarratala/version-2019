def roman_to_decimal(roman_number):
    #if roman_number == 'I':
    #    return 1
    #else:
    #    return 2
    decimal_number=0
    for letter in roman_number:
         if letter == 'I':
             decimal_number +=1
         if letter == 'V':
             decimal_number +=5     
         if letter == 'X':
             decimal_number +=10    
         if letter == 'L':
             decimal_number +=50
         if letter == 'C':
             decimal_number +=100          

    return decimal_number         