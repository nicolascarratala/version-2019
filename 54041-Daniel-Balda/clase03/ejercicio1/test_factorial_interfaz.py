import unittest
from interfaz import isnumber

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_factorial_5(self):
        result = isnumber(5)
        self.assertEqual(result, 120)

    def test_interfaz_factorial_hola(self):
            result = isnumber("hola")
            self.assertEqual(result, "ERROR")

if __name__ == '__main__':
    unittest.main()