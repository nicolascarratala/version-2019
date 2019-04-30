import unittest
from dec import deca


class TestDecimal(unittest.TestCase):

    def test_decimal_1(self):
        result = deca('1')
        self.assertEqual(result, 1)

    def test_decimal_2(self):
        result = deca('e')
        self.assertEqual(result, 14)

    def test_decimal_3(self):
        result = deca('35b1a')
        self.assertEqual(result, 219930)

    def test_decimal_4(self):
        result = deca('ff')
        self.assertEqual(result, 255)

if __name__ == '__main__':
    unittest.main()