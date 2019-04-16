import unittest
from factorial import factorial
from interfaz import interfaz

class interfaz_test(unittest.TestCase):
    def test_interfaz_5(self):
        n = interfaz(5)
        self.assertEqual(n,120)

    def test_interfaz_hola(self):
        n = interfaz("hola")
        self.assertEqual(n,"error")
        
if __name__ == '__main__':
    unittest.main()
