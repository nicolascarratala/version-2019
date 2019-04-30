import unittest
from hexa_to_decimal import hexadecimal


class TestHexadecimal(unittest.TestCase):
    def test_hexa_4(self):
        result = hexadecimal('4')
        self.assertEqual(result, 4)

    def test_hexa_8(self):
        result = hexadecimal('8')
        self.assertEqual(result, 8)

    def test_hexa_15(self):
        result = hexadecimal('F')
        self.assertEqual(result, 15)

    def test_hexa_321(self):
        result = hexadecimal('321')
        self.assertEqual(result, 801)

    def test_hexa_4D2(self):
        result = hexadecimal('4D2')
        self.assertEqual(result, 1234)

    def test_hexa_FFF(self):
        result = hexadecimal('FFF')
        self.assertEqual(result, 4095)

    def test_hexa_20F(self):
        result = hexadecimal('20F')
        self.assertEqual(result, 527)

    def test_hexa_617(self):
        result = hexadecimal('617')
        self.assertEqual(result, 1559)




if __name__ == '__main__':
    unittest.main()