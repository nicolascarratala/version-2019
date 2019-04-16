import unittest

from ronam_numbers import (
    roman_to_decimal,
    decimal_to_roman,
)




class TestRomanNumbers(unittest.TestCase):

    def test_roman_I_to_decimal(self):

        decimal_number = roman_to_decimal('I')

        self.assertEqual(decimal_number, 1)
    
    def test_roman_II_to_decimal(self):

        decimal_number = roman_to_decimal('II')

        self.assertEqual(decimal_number, 2)
    
    def test_roman_III_to_decimal(self):

        decimal_number = roman_to_decimal('III')

        self.assertEqual(decimal_number, 3)

    def test_roman_V_to_decimal(self):

        decimal_number = roman_to_decimal('V')

        self.assertEqual(decimal_number,5)

    def test_roman_VI_to_decimal(self):

        decimal_number = roman_to_decimal('VI')

        self.assertEqual(decimal_number,6)

    def test_roman_VII_to_decimal(self):

        decimal_number = roman_to_decimal('VII')

        self.assertEqual(decimal_number,7)

    def test_roman_VIII_to_decimal(self):

        decimal_number = roman_to_decimal('VIII')

        self.assertEqual(decimal_number,8)

    def test_roman_X_to_decimal(self):

        decimal_number = roman_to_decimal('X')

        self.assertEqual(decimal_number,10)

    def test_roman_XI_to_decimal(self):

        decimal_number = roman_to_decimal('XI')

        self.assertEqual(decimal_number,11)

    def test_roman_XII_to_decimal(self):

        decimal_number = roman_to_decimal('XII')

        self.assertEqual(decimal_number,12)

    def test_roman_XIII_to_decimal(self):

        decimal_number = roman_to_decimal('XIII')

        self.assertEqual(decimal_number,13)

    def test_roman_XV_to_decimal(self):

        decimal_number = roman_to_decimal('XV')

        self.assertEqual(decimal_number,15)
    def test_roman_IV_to_decimal(self):

        decimal_number = roman_to_decimal('IV')

        self.assertEqual(decimal_number,4)
    def test_roman_XIV_to_decimal(self):

        decimal_number = roman_to_decimal('XIV')
        self.assertEqual(decimal_number,14)    
    def test_roman_XIX_to_decimal(self):

        decimal_number = roman_to_decimal('XIX')
        self.assertEqual(decimal_number,19)    
    def test_roman_XVI_to_decimal(self):

        decimal_number = roman_to_decimal('XVI')
        self.assertEqual(decimal_number,16)
    def test_roman_XVII_to_decimal(self):

        decimal_number = roman_to_decimal('XVII')
        self.assertEqual(decimal_number,17)
    def test_roman_XVIII_to_decimal(self):

        decimal_number = roman_to_decimal('XVIII')
        self.assertEqual(decimal_number,18)
    def test_roman_XXIV_to_decimal(self):

        decimal_number = roman_to_decimal('XXIV')
        self.assertEqual(decimal_number,24)
    def test_roman_XLIII_to_decimal(self):

        decimal_number = roman_to_decimal('XLIII')
        self.assertEqual(decimal_number,43)    
    def test_roman_LVIII_to_decimal(self):

        decimal_number = roman_to_decimal('LVIII')
        self.assertEqual(decimal_number,58)
    def test_roman_LXXII_to_decimal(self):

        decimal_number = roman_to_decimal('LXXII')
        self.assertEqual(decimal_number,72)

    def test_roman_LXXXVII_to_decimal(self):

        decimal_number = roman_to_decimal('LXXXVII')
        self.assertEqual(decimal_number,87)
    def test_roman_XCI_to_decimal(self):
        decimal_number = roman_to_decimal('XCI')
        self.assertEqual(decimal_number,91)

    def test_roman_XCIX_to_decimal(self):

        decimal_number = roman_to_decimal('XCIX')
        self.assertEqual(decimal_number,99)
    def test_roman_CI_to_decimal(self):

        decimal_number = roman_to_decimal('CI')
        self.assertEqual(decimal_number,101)

    def test_roman_CXLIX_to_decimal(self):

        decimal_number = roman_to_decimal('CXLIX')
        self.assertEqual(decimal_number,149)

    def test_roman_CDLXXVIII_to_decimal(self):

        decimal_number = roman_to_decimal('CDLXXVIII')
        self.assertEqual(decimal_number,478)

    def test_roman_DCXCIII_to_decimal(self):

        decimal_number = roman_to_decimal('DCXCIII')
        self.assertEqual(decimal_number,693)  
    def test_roman_CMLIV_to_decimal(self):

        decimal_number = roman_to_decimal('CMLIV')
        self.assertEqual(decimal_number,954)                

class TestDecimalToRomanNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
       roman_number = decimal_to_roman(1)
       self.assertEqual(roman_number, 'I')
    def test_decimal_4_to_roman(self):
       roman_number = decimal_to_roman(4)
       self.assertEqual(roman_number, 'IV')
    def test_decimal_16_to_roman(self):
       roman_number = decimal_to_roman(16)
       self.assertEqual(roman_number, 'XVI')      
    def test_decimal_10_to_roman(self):
       roman_number = decimal_to_roman(10)
       self.assertEqual(roman_number, 'X')
    def test_decimal_14_to_roman(self):
       roman_number = decimal_to_roman(14)
       self.assertEqual(roman_number, 'XIV')    
    def test_decimal_20_to_roman(self):
       roman_number = decimal_to_roman(14)
       self.assertEqual(roman_number, 'XIV')    
    def test_decimal_24_to_roman(self):
       roman_number = decimal_to_roman(24)
       self.assertEqual(roman_number, 'XXIV')
    def test_decimal_25_to_roman(self):
       roman_number = decimal_to_roman(25)
       self.assertEqual(roman_number, 'XXV')
    def test_decimal_26_to_roman(self):
       roman_number = decimal_to_roman(26)
       self.assertEqual(roman_number, 'XXVI')
    def test_decimal_47_to_roman(self):
       roman_number = decimal_to_roman(47)
       self.assertEqual(roman_number, 'XLVII')       
    def test_decimal_59_to_roman(self):
       roman_number = decimal_to_roman(59)
       self.assertEqual(roman_number, 'LIX')  
    def test_decimal_61_to_roman(self):
       roman_number = decimal_to_roman(61)
       self.assertEqual(roman_number, 'LXI')  
    def test_decimal_77_to_roman(self):
       roman_number = decimal_to_roman(77)
       self.assertEqual(roman_number, 'LXXVII')  
    def test_decimal_177_to_roman(self):
       roman_number = decimal_to_roman(177)
       self.assertEqual(roman_number, 'CLXXVII')  
    def test_decimal_100_to_roman(self):
       roman_number = decimal_to_roman(100)
       self.assertEqual(roman_number, 'C')   
    def test_decimal_101_to_roman(self):
       roman_number = decimal_to_roman(101)
       self.assertEqual(roman_number, 'CI')   
    def test_decimal_120_to_roman(self):
       roman_number = decimal_to_roman(120)
       self.assertEqual(roman_number, 'CXX') 
    def test_decimal_582_to_roman(self):
       roman_number = decimal_to_roman(582)
       self.assertEqual(roman_number, 'DLXXXII')    
    def test_decimal_1000_to_roman(self):
       roman_number = decimal_to_roman(1000)
       self.assertEqual(roman_number, 'M')   





if __name__ == '__main__':

   unittest.main()