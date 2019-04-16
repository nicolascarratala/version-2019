import unittest

from interfaz import interfaz

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_factorial_hola(self):
        result = interfaz("hola")
        self.assertEqual(result,'ERROR')
        
if __name__ == '__main__':
    unittest.main()