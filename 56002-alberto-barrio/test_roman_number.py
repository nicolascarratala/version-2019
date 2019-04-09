import unittest #como las librerias

from ronam_numbers import roman_to_decimal
from numbers_roman import decimal_to_roman

#Test de numero romano a decimal
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
    
    def test_roman_IV_to_decimal(self):
        decimal_number = roman_to_decimal('IV')
        self.assertEqual(decimal_number, 4)

    def test_roman_V_to_decimal(self):
        decimal_number = roman_to_decimal('V')
        self.assertEqual(decimal_number, 5)
    
    def test_roman_VI_to_decimal(self):
        decimal_number = roman_to_decimal('VI')
        self.assertEqual(decimal_number, 6)
    
    def test_roman_VII_to_decimal(self):
        decimal_number = roman_to_decimal('VII')
        self.assertEqual(decimal_number, 7)

    def test_roman_VIII_to_decimal(self):
        decimal_number = roman_to_decimal('VIII')
        self.assertEqual(decimal_number, 8)

    def test_roman_IX_to_decimal(self):
        decimal_number = roman_to_decimal('IX')
        self.assertEqual(decimal_number, 9)

    def test_roman_X_to_decimal(self):
        decimal_number = roman_to_decimal('X')
        self.assertEqual(decimal_number, 10)

    def test_roman_XI_to_decimal(self):
        decimal_number = roman_to_decimal('XI')
        self.assertEqual(decimal_number, 11)

    def test_roman_XIV_to_decimal(self):
        decimal_number = roman_to_decimal('XIV')
        self.assertEqual(decimal_number, 14)
    
    def test_roman_XXIV_to_decimal(self):
        decimal_number = roman_to_decimal('XXIV')
        self.assertEqual(decimal_number, 24)

    def test_roman_XL_to_decimal(self):
        decimal_number = roman_to_decimal('XL')
        self.assertEqual(decimal_number, 40)
    
    def test_roman_XLIII_to_decimal(self):
        decimal_number = roman_to_decimal('XLIII')
        self.assertEqual(decimal_number, 43) 

    def test_roman_LVIII_to_decimal(self):
        decimal_number = roman_to_decimal('LVIII')
        self.assertEqual(decimal_number, 58)

    def test_roman_LXXII_to_decimal(self):
        decimal_number = roman_to_decimal('LXXII')
        self.assertEqual(decimal_number, 72)

    def test_roman_XCI_to_decimal(self):
        decimal_number = roman_to_decimal('XCI')
        self.assertEqual(decimal_number, 91)
    
    def test_roman_XCIX_to_decimal(self):
        decimal_number = roman_to_decimal('XCIX')
        self.assertEqual(decimal_number, 99)
    
    def test_roman_CDLXXVIII_to_decimal(self):
        decimal_number = roman_to_decimal('CDLXXVIII')
        self.assertEqual(decimal_number, 478)
        
    def test_roman_DCXCIII_to_decimal(self):
        decimal_number = roman_to_decimal('DCXCIII')
        self.assertEqual(decimal_number, 693)  
    
    def test_roman_CMLIV_to_decimal(self):
        decimal_number = roman_to_decimal('CMLIV')
        self.assertEqual(decimal_number, 954)  

#Test de numero decimal a Romano

class TestDecimalToRomanNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman(2)
        self.assertEqual(roman_number, 'II') 

    def test_decimal_3_to_roman(self):
        roman_number = decimal_to_roman(3)
        self.assertEqual(roman_number, 'III')
        
    def test_decimal_4_to_roman(self):
        roman_number = decimal_to_roman(4)
        self.assertEqual(roman_number, 'IV') 
        
    def test_decimal_5_to_roman(self):
        roman_number = decimal_to_roman(5)
        self.assertEqual(roman_number, 'V') 
        
    def test_decimal_6_to_roman(self):
        roman_number = decimal_to_roman(6)
        self.assertEqual(roman_number, 'VI') 
        
    def test_decimal_7_to_roman(self):
        roman_number = decimal_to_roman(7)
        self.assertEqual(roman_number, 'VII') 
        
    def test_decimal_8_to_roman(self):
        roman_number = decimal_to_roman(8)
        self.assertEqual(roman_number, 'VIII') 
        
    def test_decimal_9_to_roman(self):
        roman_number = decimal_to_roman(9)
        self.assertEqual(roman_number, 'IX') 
        
    def test_decimal_10_to_roman(self):
        roman_number = decimal_to_roman(10)
        self.assertEqual(roman_number, 'X') 
    
    def test_decimal_11_to_roman(self):
        roman_number = decimal_to_roman(11)
        self.assertEqual(roman_number, 'XI')      
    

if __name__ == '__main__':
    unittest.main()