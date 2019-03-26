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