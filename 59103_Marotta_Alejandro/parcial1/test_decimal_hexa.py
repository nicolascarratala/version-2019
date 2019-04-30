import unittest
from decimal_hexa import decimal_hexadecimal

class TestHexadecimal(unittest.TestCase):

    def test_decimal_5(self):
        result = decimal_hexadecimal(5)
        self.assertEqual(result,'5')
    def test_decimal_10(self):
        result = decimal_hexadecimal(10)
        self.assertEqual(result, 'A')
    
    def test_decimal_17(self):
        result = decimal_hexadecimal(17)
        self.assertEqual(result, '11')
    def test_decimal_16(self):
        result = decimal_hexadecimal(16)
        self.assertEqual(result, '10')
    def test_decimal_4095(self):
        result = decimal_hexadecimal(4095)
        self.assertEqual(result, 'FFF')    
    def test_decimal_1234(self):
        result = decimal_hexadecimal(1234)
        self.assertEqual(result, '4D2')
    def test_decimal_234(self):
        result = decimal_hexadecimal(234)
        self.assertEqual(result, 'EA')
    
    
    
    
if __name__ == '__main__':
  unittest.main()