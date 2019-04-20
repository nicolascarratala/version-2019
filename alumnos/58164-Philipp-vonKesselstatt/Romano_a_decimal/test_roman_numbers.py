import unittest
from ronam_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('DCCXIX')
        self.assertEqual(decimal_number, 719)
if __name__ == '__main__':
    unittest.main()
