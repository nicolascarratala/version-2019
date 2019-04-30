import unittest
from interfaz import decimal

class Test_Interfaz(unittest.TestCase):
    def test_interfaz_number1(self):
        number=decimal("hola")
        self.assertEqual(number,"Disculpe,solo acepto numeros")

if __name__ == '__main__':
    unittest.main()