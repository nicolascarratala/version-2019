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
      if letter== 'L':
         if k==0:
            decimal_number=decimal_number+50
         else:
            decimal_number=decimal_number-2+50
            k=0
      if letter== 'C':
         if k==0:
            decimal_number=decimal_number+100
         else:
            decimal_number=decimal_number-2+100
            k=0
      if letter== 'D':
         if k==0:
            decimal_number=decimal_number+500
         else:
            decimal_number=decimal_number-2+500
            k=0
      if letter== 'M':
         if k==0:
            decimal_number=decimal_number+1000
         else:
            decimal_number=decimal_number-2+1000
            k=0
            
   return decimal_number