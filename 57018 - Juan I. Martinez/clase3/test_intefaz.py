import unittest
from interfaz import interfaz_factorial


class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_factorial_1(self):
        result = interfaz_factorial(5)
        self.assertEqual(result, 120)

    def test_interfaz_factorial_2(self):
        result = interfaz_factorial("asd")
        self.assertEqual(result, "Error")


if __name__ == '__main__':
    unittest.main()