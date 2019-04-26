import unittest
from cifrado_vigenere import cifrar_v

class Test_Cifrado_Vigenere(unittest.TestCase):
    def test_cifrado(self):
        cifrados=cifrar_v('HOLA', 'LINE')
        self.assertEqual(cifrados, 'SWYE')

if __name__ == '__main__':
    unittest.main()