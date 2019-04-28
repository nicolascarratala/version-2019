import unittest
from Decimal_to_Ex import   Convert

class Test_Decimal_to_Ex(unittest.TestCase):
    def test_decimal_to_ex_number0(self):
        number=Convert(5)
        self.assertEqual(number,5)
    def test_decimal_to_ex_number1(self):
        number=Convert(10)
        self.assertEqual(number,'A')
    def test_decimal_to_ex_number2(self):
        number=Convert(12)
        self.assertEqual(number,'C')
    def test_decimal_to_ex_number3(self):
        number=Convert(4095)
        self.assertEqual(number,'FFF')
    def test_decimal_to_ex_number4(self):
        number=Convert(1234)
        self.assertEqual(number,'4D2')
    def test_decimal_to_ex_number5(self):
        number=Convert(-1)
        self.assertEqual(number,0)


if __name__ == '__main__':
    unittest.main()