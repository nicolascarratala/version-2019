def roman_to_decimal(roman_number):
   decimal_number=0
   k=0
   for letter in roman_number:
      if letter== 'I':
         decimal_number=decimal_number+1
         k=k+1
      if letter== 'V':
         if k==0:
            decimal_number=decimal_number+5
         else:
            decimal_number=decimal_number-2+5 
            k=0        
      if letter== 'X':
         if k==0:
            decimal_number=decimal_number+10
         else:
            decimal_number=decimal_number-2+10
            k=0
   return decimal_number