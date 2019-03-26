import unittest

from ronam_numbers import roman_to_decimal





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
    def test_roman_LIIX_to_decimal(self):

        decimal_number = roman_to_decimal('LIIX')
        self.assertEqual(decimal_number,58)
    def test_roman_LXXII_to_decimal(self):

        decimal_number = roman_to_decimal('LXXII')
        self.assertEqual(decimal_number,72)

    def test_roman_LXXXVII_to_decimal(self):

        decimal_number = roman_to_decimal('XVIII')
        self.assertEqual(decimal_number,87)
    def test_roman_XCI_to_decimal(self):
        decimal_number = roman_to_decimal('XCI')
        self.assertEqual(decimal_number,91)

    def test_roman_IC_to_decimal(self):

        decimal_number = roman_to_decimal('IC')
        self.assertEqual(decimal_number,99)
    def test_roman_CI_to_decimal(self):

        decimal_number = roman_to_decimal('CI')
        self.assertEqual(decimal_number,101)
    def test_roman_CXLIX_to_decimal(self):

        decimal_number = roman_to_decimal('CXLIX')
        self.assertEqual(decimal_number,149)     
    def test_roman_CLDXXVIII_to_decimal(self):

        decimal_number = roman_to_decimal('CLDXXVIII')
        self.assertEqual(decimal_number,478)
    def test_roman_DCXCIII_to_decimal(self):

        decimal_number = roman_to_decimal('DCXCIII')
        self.assertEqual(decimal_number,693)  
    def test_roman_CMLIV_to_decimal(self):

        decimal_number = roman_to_decimal('CMLIV')
        self.assertEqual(decimal_number,954)                     
if __name__ == '__main__':

   unittest.main()