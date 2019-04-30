#Juan I. Martinez, Legajo 57018

import unittest
from hexa_a_dec import conversor

class TestConversor(unittest.TestCase):
    def test_conversor_1(self):
        result = conversor(1)
        self.assertEqual(result, 1)

    def test_conversor_2(self):
        result = conversor('a')
        self.assertEqual(result, 10)

    def test_conversor_3(self):
        result = conversor("3E7")
        self.assertEqual(result, 999)

    def test_conversor_4(self):
        result = conversor("11")
        self.assertEqual(result, 17)

    def test_conversor_5(self):
        result = conversor("10")
        self.assertEqual(result, 16)

    def test_conversor_6(self):
        result = conversor("FFF")
        self.assertEqual(result, 4095)
    
    def test_conversor_7(self):
        result = conversor("4D2")
        self.assertEqual(result, 1234)

    def test_conversor_8(self):
        result = conversor("EA")
        self.assertEqual(result, 234)

    def test_conversor_9(self):
        result = conversor(5)
        self.assertEqual(result, 5)        

    def test_conversor_10(self):
        result = conversor("yub")
        self.assertEqual(result, "Caracter/es incorrecto/s")    

    def test_conversor_11(self):
        result = conversor("??")
        self.assertEqual(result, "Caracter/es incorrecto/s")        


if __name__ == '__main__':
    unittest.main()