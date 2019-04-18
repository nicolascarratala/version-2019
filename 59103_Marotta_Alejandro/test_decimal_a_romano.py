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
    
    def test_24(self):
        romanotest = decimal_a_romano(24)
        self.assertEqual(romanotest,'XXIV')
    def test_43(self):
        romanotest = decimal_a_romano(43)
        self.assertEqual(romanotest,'XLIII')
    def test_58(self):
        romanotest = decimal_a_romano(58)
        self.assertEqual(romanotest,'LVIII')  
        
    def test_69 (self):
        romanotest = decimal_a_romano(69)
        self.assertEqual(romanotest, 'LXIX')

    def test_72 (self):
        romanotest = decimal_a_romano(72)
        self.assertEqual(romanotest,'LXXII')    
    
    
    def test_99 (self):
        romanotest = decimal_a_romano(99)
        self.assertEqual(romanotest, 'XCIX')

    def test_100 (self):
        romanotest = decimal_a_romano(100)
        self.assertEqual(romanotest, 'C')

    def test_102 (self):
        romanotest = decimal_a_romano(102)
        self.assertEqual(romanotest, 'CII')

    def test_125 (self):
        romanotest = decimal_a_romano(125)
        self.assertEqual(romanotest, 'CXXV')

    def test_149 (self):
        romanotest = decimal_a_romano(149)
        self.assertEqual(romanotest, 'CXLIX')
    

    def test_200 (self):
        romanotest = decimal_a_romano(200)
        self.assertEqual(romanotest, 'CC')

    def test_258 (self):
        romanotest = decimal_a_romano(258)
        self.assertEqual(romanotest, 'CCLVIII')


    def test_478 (self):
        romanotest = decimal_a_romano(478)
        self.assertEqual(romanotest, 'CDLXXVIII')

    def test_693 (self):
        romanotest = decimal_a_romano(693)
        self.assertEqual(romanotest, 'DCXCIII')

   
    def test_954 (self):
        romanotest = decimal_a_romano(954)
        self.assertEqual(romanotest, 'CMLIV')

    def test_999 (self):
        romanotest = decimal_a_romano(999)
        self.assertEqual(romanotest, 'CMXCIX')


    def test_1359 (self):
        romanotest = decimal_a_romano(1359)
        self.assertEqual(romanotest, 'MCCCLIX')

    def test_1416 (self):
        romanotest = decimal_a_romano(1416)
        self.assertEqual(romanotest, 'MCDXVI')

    def test_2307 (self):
        romanotest = decimal_a_romano(2307)
        self.assertEqual(romanotest, 'MMCCCVII')
    

    def test_2579 (self):
        romanotest = decimal_a_romano(2579)
        self.assertEqual(romanotest, 'MMDLXXIX')

    def test_3091 (self):
        romanotest = decimal_a_romano(3091)
        self.assertEqual(romanotest, 'MMMXCI')

    def test_3707 (self):
        romanotest = decimal_a_romano(3707)
        self.assertEqual(romanotest, 'MMMDCCVII')


    

    def test_3833(self):
        romanotest = decimal_a_romano(3833)
        self.assertEqual(romanotest,'MMMDCCCXXXIII')


    
    def test_3999(self):
        romanotest = decimal_a_romano(3999)
        self.assertEqual(romanotest,'MMMCMXCIX')





    

    

    
    


    
    




if __name__ == '__main__':
   unittest.main()