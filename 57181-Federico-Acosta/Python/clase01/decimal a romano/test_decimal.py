import unittest
import array as arr
from decimal_numbers import decimal_to_roman

class TestDecimal(unittest.TestCase):
    
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman(1)
        print(roman_number)
        self.assertEqual(roman_number,'I')
    
    def test_decimal_3_to_roman(self):
        roman_number = decimal_to_roman(3)
        print(roman_number)
        self.assertEqual(roman_number,'III')
    
    def test_decimal_10_to_roman(self):
        roman_number = decimal_to_roman(10)
        print(roman_number)
        self.assertEqual(roman_number,'X')
    
    def test_decimal_4_to_roman(self):
        roman_number = decimal_to_roman(4)
        print(roman_number)
        self.assertEqual(roman_number,'IV')
    
    def test_decimal_14_to_roman(self):
        roman_number = decimal_to_roman(14)
        print(roman_number)
        self.assertEqual(roman_number,'XIV')
    
    def test_decimal_54_to_roman(self):
        roman_number = decimal_to_roman(54)
        print(roman_number)
        self.assertEqual(roman_number,'LIV')
    def test_decimal_4444_to_roman(self):
        roman_number = decimal_to_roman(4444)
        print(roman_number)
        self.assertEqual(roman_number,'IVCDXLIV')
    def test_decimal_468_to_roman(self):
        roman_number = decimal_to_roman(468)
        print(roman_number)
        self.assertEqual(roman_number,'CDLXVIII')
    def test_decimal_7748_to_roman(self):
        roman_number = decimal_to_roman(7748)
        print(roman_number)
        self.assertEqual(roman_number,'VMMDCCXLVIII')
    def test_decimal_958_to_roman(self):
        roman_number = decimal_to_roman(958)
        print(roman_number)
        self.assertEqual(roman_number,'CMLVIII')

#q = 'hola '
#w = 'que tal'
#e = q + w 
#print(e)
#a = [1,2,3]
#print(*a, sep="")
#a.append(4)
#print(*a, sep="")

if __name__ =='__main__':
    unittest.main()