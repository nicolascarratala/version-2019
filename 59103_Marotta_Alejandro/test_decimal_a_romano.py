import unittest
from decimal_a_romano import decimal_a_romano

class TestDecimal(unittest.TestCase):
    def test_1 (self):
        romanotest = decimal_a_romano('1')
        self.assertEqual(romanotest, 'I')


    def test_2 (self):
        romanotest = decimal_a_romano('2')
        self.assertEqual(romanotest, 'II')
        
    def test_3 (self):
        romanotest = decimal_a_romano('3')
        self.assertEqual(romanotest, 'III')

    def test_4 (self):
        romanotest = decimal_a_romano('4')
        self.assertEqual(romanotest, 'IV')

    def test_5 (self):
        romanotest = decimal_a_romano('5')
        self.assertEqual(romanotest, 'V')














if __name__ == '__main__':
   unittest.main()