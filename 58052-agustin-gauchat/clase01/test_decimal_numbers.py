import unittest
from decilam_numbers import decimal_to_roman

class TestsDecimalNumbers(unittest.TestCase) :

    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman(1)
        self.assertEqual(roman_number, "I")

    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman(2)
        self.assertEqual(roman_number, "II")

    def test_decimal_3_to_roman(self):
        roman_number = decimal_to_roman(3)
        self.assertEqual(roman_number, "III")

    def test_decimal_4_to_roman(self):
        roman_number = decimal_to_roman(4)
        self.assertEqual(roman_number, "IV")

    def test_decimal_9_to_roman(self):
        roman_number = decimal_to_roman(9)
        self.assertEqual(roman_number, "IX")

    def test_decimal_24_to_roman(self):
        roman_number = decimal_to_roman(24)
        self.assertEqual(roman_number, "XXIV")

    def test_decimal_43_to_roman(self):
        roman_number = decimal_to_roman(43)
        self.assertEqual(roman_number, "XLIII")

    def test_decimal_58_to_roman(self):
        roman_number = decimal_to_roman(58)
        self.assertEqual(roman_number, "LVIII")

    def test_decimal_72_to_roman(self):
        roman_number = decimal_to_roman(72)
        self.assertEqual(roman_number, "LXXII")

    def test_decimal_87_to_roman(self):
        roman_number = decimal_to_roman(87)
        self.assertEqual(roman_number, "LXXXVII")

    def test_decimal_91_to_roman(self):
        roman_number = decimal_to_roman(91)
        self.assertEqual(roman_number, "XCI")

    def test_decimal_99_to_roman(self):
        roman_number = decimal_to_roman(99)
        self.assertEqual(roman_number, "XCIX")

    def test_decimal_149_to_roman(self):
        roman_number = decimal_to_roman(149)
        self.assertEqual(roman_number, "CXLIX")

    def test_decimal_478_to_roman(self):
        roman_number = decimal_to_roman(478)
        self.assertEqual(roman_number, "CDLXXVIII")

    def test_decimal_693_to_roman(self):
        roman_number = decimal_to_roman(693)
        self.assertEqual(roman_number, "DCXCIII")

    def test_decimal_954_to_roman(self):
        roman_number = decimal_to_roman(954)
        self.assertEqual(roman_number, "CMLIV")

    def test_decimal_999_to_roman(self):
        roman_number = decimal_to_roman(999)
        self.assertEqual(roman_number, "CMXCIX")


if __name__ == '__main__':
    unittest.main()