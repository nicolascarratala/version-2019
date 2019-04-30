import unittest
from interfaz import word

class Test_interfaz(unittest.TestCase):
    def test_interfaz(self):
        clave=word("HOLA", "LINE")
        self.assertEqual(clave, "SWYE")
    def test_interfaz_number(self):
        clave=word(123, 45)
        self.assertEqual(clave, "ERROR no se ingresaron letras")


if __name__ == '__main__':
    unittest.main()