import unittest
from decilam_numbers import decimal_to_roman

class TestsDecimalNumbers(unittest.TestCase) :

    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman('1', 1)
        self.assertEqual(roman_number, "I")

    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman('2', 2)
        self.assertEqual(roman_number, "II")


if __name__ == '__main__':
    unittest.main()