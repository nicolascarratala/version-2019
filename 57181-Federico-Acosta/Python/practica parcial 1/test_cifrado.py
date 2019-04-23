import unittest
from interfaz_cifrado import interfaz_cifrador

class TestCypher(unittest.TestCase):
    
    def test_wikihowisthebest(self):
        codigo = interfaz_cifrador("wikihowisthebest","fede")
        print(codigo)
        self.assertEqual(codigo,'bmnmmszmxxkigivx')
    
    def test_wikihowisthebest2(self):
        codigo = interfaz_cifrador("wikihowisthebest","value")
        print(codigo)
        self.assertEqual(codigo,'rivcljwtmxcemywo')

    def test_exceptionTypeError(self):
        codigo = interfaz_cifrador("wikihowisthebest",256)
        print(codigo)
        self.assertEqual(codigo,"Una variable es INT Type Error")

    def test_exceptionValueError(self):
        codigo = interfaz_cifrador("wikihowisthebest","a2x5c6")
        print(codigo)
        self.assertEqual(codigo,"Hay numeros en las variables Value Error")

if __name__ =='__main__':
    unittest.main()

    