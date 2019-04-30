import unittest
from interfaz import interfaz_hexadecimal

class TestInterfaz(unittest.TestCase):
    def test_interfaz_5(self):
        result = interfaz_hexadecimal('5')
        self.assertEqual(result,'5')

    def test_interfaz_hola(self):
        result = interfaz_hexadecimal('HOLA')
        self.assertEqual(result,False)

    def test_interfaz_51(self):
        result = interfaz_hexadecimal('5.1')
        self.assertEqual(result,False)
    
    def test_interfaz_52(self):
        result = interfaz_hexadecimal('5,2')
        self.assertEqual(result,False)

    def test_interfaz_hola6000(self):
        result = interfaz_hexadecimal('6000')
        self.assertEqual(result,False)




if __name__ == '__main__':
  unittest.main()