import unittest
from decimal_a_romano import decimal_a_romano

class TestDecimal(unittest.TestCase):
    def test_1 (self):
        romanotest = decimal_a_romano(1)
        self.assertEqual(romanotest, 'I')


    def test_2 (self):
        romanotest = decimal_a_romano(2)
        self.assertEqual(romanotest, 'II')
    def test_3 (self):
        romanotest = decimal_a_romano(3)
        self.assertEqual(romanotest, 'III')
    def test_4 (self):
        romanotest = decimal_a_romano(4)
        self.assertEqual(romanotest, 'IV')
    def test_5 (self):
        romanotest = decimal_a_romano(5)
        self.assertEqual(romanotest, 'V')
    def test_6 (self):
        romanotest = decimal_a_romano(6)
        self.assertEqual(romanotest, 'VI')
    def test_7 (self):
        romanotest = decimal_a_romano(7)
        self.assertEqual(romanotest, 'VII')
    def test_8 (self):
        romanotest = decimal_a_romano(8)
        self.assertEqual(romanotest, 'VIII')
    def test_9 (self):
        romanotest = decimal_a_romano(9)
        self.assertEqual(romanotest, 'IX')

    def test_10(self):
        romanotest = decimal_a_romano(10)
        self.assertEqual(romanotest, 'X')

    def test_11 (self):
        romanotest = decimal_a_romano(11)
        self.assertEqual(romanotest, 'XI')
    def test_12 (self):
        romanotest = decimal_a_romano(12)
        self.assertEqual(romanotest, 'XII')
    def test_13 (self):
        romanotest = decimal_a_romano(13)
        self.assertEqual(romanotest, 'XIII')
    def test_14 (self):
        romanotest = decimal_a_romano(14)
        self.assertEqual(romanotest, 'XIV')
    def test_15 (self):
        romanotest = decimal_a_romano(15)
        self.assertEqual(romanotest, 'XV')
    def test_16 (self):
        romanotest = decimal_a_romano(16)
        self.assertEqual(romanotest, 'XVI')
    def test_17 (self):
        romanotest = decimal_a_romano(17)
        self.assertEqual(romanotest, 'XVII')
    def test_18 (self):
        romanotest = decimal_a_romano(18)
        self.assertEqual(romanotest, 'XVIII')
    def test_19 (self):
        romanotest = decimal_a_romano(19)
        self.assertEqual(romanotest, 'XIX')
    def test_20 (self):
        romanotest = decimal_a_romano(20)
        self.assertEqual(romanotest, 'XX')
    

    def test_99 (self):
        romanotest = decimal_a_romano(99)
        self.assertEqual(romanotest, 'XCIX')
    




if __name__ == '__main__':
   unittest.main()