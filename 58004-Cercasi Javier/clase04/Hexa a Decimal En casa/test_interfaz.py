import unittest
from interfaz import interfaz


class TestInterfaz(unittest.TestCase):
    def test_hexa_15(self):
        result = interfaz('F')
        self.assertEqual(result, 15)

    def test_hexa_321(self):
        result = interfaz('321')
        self.assertEqual(result, 801)

    def test_hexa_4D2(self):
        result = interfaz('4D2')
        self.assertEqual(result, 1234)

    def test_hexa_Vacio(self):
        result = interfaz('')
        self.assertEqual(result, 'Error1')

    def test_hexa_Hola(self):
        result = interfaz('Hola')
        self.assertEqual(result, 'Error2')

    
if __name__ == '__main__':
    unittest.main()

    