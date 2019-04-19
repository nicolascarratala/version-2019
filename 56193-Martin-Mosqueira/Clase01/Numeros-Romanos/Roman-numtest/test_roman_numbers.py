import unittest
from ronam_numbers import roman_to_decimal

class TestRomanNumbers(unittest.TestCase):
    def test_roman_i_to_decimal(self):
        decimal_numbers = roman_to_decimal('i')
        self.assertEqual(decimal_numbers,1)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('ii')
        self.assertEqual(decimal_numbers,2)
    def test_roman_iii_to_decimal(self):
        decimal_numbers = roman_to_decimal('iii')
        self.assertEqual(decimal_numbers,3)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('iv')
        self.assertEqual(decimal_numbers,4)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('v')
        self.assertEqual(decimal_numbers,5)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('vi')
        self.assertEqual(decimal_numbers,6)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('vii')
        self.assertEqual(decimal_numbers,7)
    def test_roman_ii_to_decimal(self):
         decimal_numbers = roman_to_decimal('viii')
         self.assertEqual(decimal_numbers,8)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('ix')
        self.assertEqual(decimal_numbers,9)
    def test_roman_ii_to_decimal(self):
        decimal_numbers = roman_to_decimal('x')
        self.assertEqual(decimal_numbers,10)
    def test_roman_xliii_to_decimal(self):
        decimal_numbers = roman_to_decimal('xliii')
        self.assertEqual(decimal_numbers,43)
    def test_roman_lviii_to_decimal(self):
        decimal_numbers = roman_to_decimal('lviii')
        self.assertEqual(decimal_numbers,58)
    def test_roman_mccc_to_decimal(self):
        decimal_numbers = roman_to_decimal('mccc')
        self.assertEqual(decimal_numbers,1300)

if __name__ == '__main__' :
    unittest.main()

