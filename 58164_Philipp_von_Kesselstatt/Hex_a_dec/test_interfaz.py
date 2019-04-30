import unittest
from interfaz import interfaz


class TestDecimal(unittest.TestCase):

    def test_decimal_1(self):
        result = interfaz('1')
        self.assertEqual(result, 1)

    def test_decimal_2(self):
        result = interfaz('e')
        self.assertEqual(result, 14)

    def test_decimal_3(self):
        result = interfaz('35b1a')
        self.assertEqual(result, 219930)

    def test_decimal_4(self):
        result = interfaz('ff')
        self.assertEqual(result, 255)

    def test_decimal_5(self):
        result = interfaz('')
        self.assertEqual(result, 'ingrese un numero')

    def test_decimal_6(self):
        result = interfaz('-17')
        self.assertEqual(result, 'ingrese un numero hexadecimal positivo')

    def test_decimal_7(self):
        result = interfaz('<s6b-!')
        self.assertEqual(result, 'el numero debe ser un hexadecimal positivo')

    def test_decimal_8(self):
        result = interfaz('u')
        self.assertEqual(result, 'el numero debe ser un hexadecimal positivo')

if __name__ == '__main__':
    unittest.main()