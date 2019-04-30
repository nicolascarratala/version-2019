def hexa_digit_to_decimal(hexa_digit):
    if hexa_digit.isdecimal():
       dec = int(hexa_digit)

    if hexa_digit.isalpha():
       if hexa_digit == 'A':
           dec = 10
       elif hexa_digit == 'B':
           dec = 11
       elif hexa_digit == 'C':
           dec = 12
       elif hexa_digit == 'D':
           dec = 13
       elif hexa_digit == 'E':
           dec = 14
       elif hexa_digit == 'F':
           dec = 15
       else:
           dec = 0
    return dec

def hexadecimal_to_decimal(hexadec):
    dec = 0
    decimal_number = 0
    n = 0
    hexadec = hexadec[::-1]
    count = len(hexadec)
    for n in range(count):
       dec = hexa_digit_to_decimal(hexadec[n])
       decimal_number += dec*pow(16,n)

    return str(decimal_number)


'''def hexadecimal_to_decimal(hexadec):
    
    dec = 0

    decimal_number = 0

    n = 0

    hexadec = hexadec[::-1]

    count = len(hexadec)

    for n in range(count):

        if hexadec[n].isdecimal() == True:

            dec = int(hexadec[n])

        if hexadec[n].isalpha() == True:

            if hexadec[n] == 'A':

                dec = 10

            elif hexadec[n] == 'B':

                dec = 11

            elif hexadec[n] == 'C':

                dec = 12

            elif hexadec[n] == 'D':

                dec = 13

            elif hexadec[n] == 'E':

                dec = 14

            elif hexadec[n] == 'F':

                dec = 15

            else:

                dec = 0

                decimal_number = 0

        decimal_number += dec*pow(16,n)

        

    return str(decimal_number)'''