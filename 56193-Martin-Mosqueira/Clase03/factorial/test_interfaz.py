import unittest
from interfaz import isnumber

class Test_Interfaz_Factorial(unittest.TestCase):
    def test_interfaz(self):
        resultado=isnumber(6)
        self.assertEqual(resultado,720)
    def test_interfaz(self):
        resultado=isnumber("hola")
        self.assertEqual(resultado,"ERROR")

if __name__ == '__main__':
    unittest.main()