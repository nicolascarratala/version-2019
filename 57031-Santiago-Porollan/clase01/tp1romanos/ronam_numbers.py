def roman_to_decimal(roman_number):
   decimal_number=0
   counter=0
   for letter in roman_number:

      if letter== 'I':
         decimal_number=decimal_number+1

      if letter== 'V':
         decimal_number=decimal_number+5
         if counter != 0:
            if roman_number[counter-1] == "I":
               decimal_number=decimal_number-2
                           
      if letter== 'X':
         decimal_number=decimal_number+10
         if counter != 0:
            if roman_number[counter-1] == 'I':
               decimal_number=decimal_number-2

      if letter== 'L':
         decimal_number=decimal_number+50
         if counter != 0:
            if roman_number[counter-1] == 'X':
               decimal_number=decimal_number-20

      if letter== 'C':
         decimal_number=decimal_number+100
         if counter != 0:
            if roman_number[counter-1] == 'X' :
               decimal_number=decimal_number-20

      if letter== 'D':
         decimal_number=decimal_number+500
         if counter != 0:
            if roman_number[counter-1]== 'C':
               decimal_number=decimal_number-200

      if letter== 'M':
         decimal_number=decimal_number+1000
         if counter != 0:
            if roman_number[counter-1]== 'D':
               decimal_number=decimal_number-1000
            elif roman_number[counter-1]== 'C':
               decimal_number=decimal_number-200       

      counter=counter+1
      
   return decimal_number

def decimal_to_roman(decimal_num):
   roman_number = ''
   counter = 0
   decimal_number = str(decimal_num)
   for number in reversed(decimal_number):

      if number == '1':
         if counter == 0:
            roman_number=roman_number+'I'
         elif counter == 1:
            roman_number='X'+roman_number
         elif counter == 2:
            roman_number='C'+roman_number
         elif counter == 3:
            roman_number='M'+roman_number

      elif number == '2':
         if counter==0:
            roman_number = roman_number + 'II'
         elif counter == 1:
            roman_number='XX' + roman_number
         elif counter == 2:
            roman_number='CC'+ roman_number
         elif counter == 3 :
            roman_number ='MM' + roman_number

      elif number == '3':
         if counter==0:
            roman_number = roman_number + 'III'
         elif counter==1:
            roman_number ='XXX' + roman_number
         elif counter==2:
            roman_number ='CCC' + roman_number

      elif number == '4':
         if counter==0:
            roman_number = roman_number + 'IV'
         elif counter==1:
            roman_number = 'XL'+roman_number
         elif counter==2:
            roman_number = 'CD'+ roman_number

      elif number == '5':
         if counter==0:
            roman_number = roman_number + 'V'
         elif counter==1:
            roman_number= 'L' +roman_number
         elif counter==2:
            roman_number= 'D' +roman_number

      elif number == '6':
         if counter==0:
            roman_number = roman_number + 'VI'
         elif counter==1:
            roman_number= 'LX' + roman_number
         elif counter== 2:
            roman_number= 'DC' +roman_number

      elif number == '7':
         if counter==0:
            roman_number = roman_number + 'VII'
         elif counter== 1:
            roman_number = 'LXX' + roman_number
         elif counter == 2:
            roman_number = 'DCC' + roman_number 
      elif number == '8':
         if counter==0:
            roman_number = roman_number + 'VIII'
         elif counter==1:
            roman_number= 'LXXX'+roman_number
         elif counter==2:
            roman_number= 'DCCC'+roman_number
      
      elif number == '9':
         if counter==0:
            roman_number = roman_number + 'IX'
         elif counter==1:
            roman_number= 'XC'+roman_number
         elif counter==2:
            roman_number= 'CM'+roman_number

      counter=counter+1
  
   return roman_number