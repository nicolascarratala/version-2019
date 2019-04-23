def roman_to_decimal(roman_number):
    decimal_number = 0
    ant = 0
    for letter in roman_number:
        
        if letter == 'I':
                decimal_number = decimal_number + 1
                ant = 'I'
        
        if letter == 'V':

            if ant == 'I':
                decimal_number = decimal_number + 3
                ant = 'V'
            else:
                ant = 'V'
                decimal_number = decimal_number + 5
               
        if letter == 'X':
            
            if ant == 'I':
                decimal_number = decimal_number + 8
                ant = 'X'
            else:
                ant = 'X'
                decimal_number = decimal_number + 10
               
        if letter == 'L':

            if ant == 'I':
                decimal_number = decimal_number + 48
                ant = 'L'
            else:
                if ant == 'X':
                    decimal_number = decimal_number + 30
                    ant = 'L'
                else:
                    ant = 'L'
                    decimal_number = decimal_number + 50

        if letter == 'C':
            
            if ant == 'I':
                decimal_number = decimal_number + 98
                ant = 'C'
            else:
                if ant == 'X':
                    decimal_number = decimal_number + 80
                    ant = 'C'
                else:
                    ant = 'C'
                    decimal_number = decimal_number + 100
        if letter == 'D':
            
            if ant == 'I':
                decimal_number = decimal_number + 498
                ant = 'D'
            else:
                if ant == 'X':
                    decimal_number = decimal_number + 480
                    ant = 'D'
                else:
                    if ant == 'C':
                        decimal_number = decimal_number + 300
                    else:
                        ant = 'D'
                        decimal_number = decimal_number + 500
        if letter == 'M':

            if ant == 'I':
                decimal_number =decimal_number + 998
                ant = 'M'
            else:
                if ant == 'X':
                    decimal_number = decimal_number + 980
                    ant = 'M'
                else:
                    if ant == 'C':
                        decimal_number = decimal_number + 800
                    else:
                        ant = 'M'
                        decimal_number = decimal_number + 1000
    return decimal_number

    
