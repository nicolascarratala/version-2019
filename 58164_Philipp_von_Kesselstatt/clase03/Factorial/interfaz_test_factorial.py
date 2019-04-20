import unittest
from interfaz import interfaz

class Testinterfaz(unittest.TestCase):

    def test_interfaz_1(self):
        result = interfaz('1')
        self.assertEqual(result, 1)
    def test_interfaz_2(self):
        
        result = interfaz ('0.5')
        self.assertEqual(result, 'ingrese un numero entero positivo')
    def test_interfaz_3(self):
        
        result = interfaz ('hola')
        self.assertEqual(result, 'ingrese un numero entero positivo')
    def test_interfaz_4(self):
        
        result = interfaz ('-17')
        self.assertEqual(result, 'ingrese un numero entero positivo')
    
        
    
if __name__ == '__main__':
    unittest.main()