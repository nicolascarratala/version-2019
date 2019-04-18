import unittest
from decimal_numbers import decimal_to_roman

class TestDecimalNumbers(unittest.TestCase):
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

    def test_decimal_15_to_roman(self):
        roman_number = decimal_to_roman(15)
        self.assertEqual(roman_number, 'XV')
    
    def test_decimal_24_to_roman(self):
        roman_number = decimal_to_roman(24)
        self.assertEqual(roman_number, 'XXIV')
    
    def test_decimal_43_to_roman(self):
        roman_number = decimal_to_roman(43)
        self.assertEqual(roman_number, 'XLIII')

    def test_decimal_58_to_roman(self):
        roman_number = decimal_to_roman(58)
        self.assertEqual(roman_number, 'LVIII')
    
    def test_decimal_72_to_roman(self):
        roman_number = decimal_to_roman(72)
        self.assertEqual(roman_number, 'LXXII') 
    
    def test_decimal_87_to_roman(self):
        roman_number = decimal_to_roman(87)
        self.assertEqual(roman_number, 'LXXXVII') 

    def test_decimal_91_to_roman(self):
        roman_number = decimal_to_roman(91)
        self.assertEqual(roman_number, 'XCI')

    def test_decimal_99_to_roman(self):
        roman_number = decimal_to_roman(99)
        self.assertEqual(roman_number, 'XCIX')
    
    def test_decimal_101_to_roman(self):
        roman_number = decimal_to_roman(101)
        self.assertEqual(roman_number, 'CI') 

    def test_decimal_149_to_roman(self):
        roman_number = decimal_to_roman(294)
        self.assertEqual(roman_number, 'CCXCIV') 

    def test_decimal_478_to_roman(self):
        roman_number = decimal_to_roman(501)
        self.assertEqual(roman_number, 'DI')

    def test_decimal_693_to_roman(self):
        roman_number = decimal_to_roman(632)
        self.assertEqual(roman_number, 'DCXXXII')
    
    def test_decimal_954_to_roman(self):
        roman_number = decimal_to_roman(904)
        self.assertEqual(roman_number, 'CMIV')    
  
    def test_decimal_999_to_roman(self):
        roman_number = decimal_to_roman(999)
        self.assertEqual(roman_number, 'CMXCIX')  

    def test_decimal_1000_to_roman(self):
        roman_number = decimal_to_roman(1000)
        self.assertEqual(roman_number, 'M')

    def test_decimal_1954_to_roman(self):
        roman_number = decimal_to_roman(1649)
        self.assertEqual(roman_number, 'MDCIL')    

    def test_decimal_3999_to_roman(self):
        roman_number = decimal_to_roman(2554)
        self.assertEqual(roman_number, 'MMDLIV') 

if __name__ == '__main__':
    unittest.main()

