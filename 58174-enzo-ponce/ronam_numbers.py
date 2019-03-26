def roman_to_decimal(roman_number):
   decimal_number = 0
   ant = 0
   for letter in roman_number:
      if letter == 'I':
         decimal_number = decimal_number + 1
   
      if letter == 'V':
         decimal_number = decimal_number +5
         if ant == 'I':
            decimal_number = decimal_number -2

      if letter == 'X':
         decimal_number = decimal_number +10
         if ant == 'I':
            decimal_number = decimal_number -2

   ant = letter

   return decimal_number