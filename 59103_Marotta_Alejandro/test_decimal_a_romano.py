import unittest
from decimal_a_romano import decimal_a_romano

class TestDecimal(unittest.TestCase):
    def test_1 (self):
        romanotest = decimal_a_romano('1')
        self.assertEqual(romanotest, 'I')












if __name__ == '__main__':
   unittest.main()