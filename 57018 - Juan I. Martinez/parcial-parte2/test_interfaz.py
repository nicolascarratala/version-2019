#Juan I. Martinez, Legajo 57018

import unittest
from interfaz import interfaz

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_1(self):
        result = interfaz("4D2")
        self.assertEqual(result, 1234)

    def test_interfaz_2(self):
        result = interfaz("HOLA")
        self.assertEqual(result, "Caracter/es incorrecto/s")
        
    def test_interfaz_3(self):
        result = interfaz("FFF")
        self.assertEqual(result, 4095)
    

if __name__ == '__main__':
    unittest.main()