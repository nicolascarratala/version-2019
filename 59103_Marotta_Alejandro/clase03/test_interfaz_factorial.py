import unittest
from factorial_interfaz import factorial_interfaz

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_factorial_5(self):
        result = factorial_interfaz("5")
        self.assertEqual(result, 120)

    def test_interfaz_factorial_12(self):
        result = factorial_interfaz("12")
        self.assertEqual(result, 479001600)

    def test_interfaz_factorial_negativo(self):
        result = factorial_interfaz("-5")
        self.assertEqual(result, "Valor no valido")

    def test_interfaz_factorial_hola(self):
        result = factorial_interfaz("hola")
        self.assertEqual(result, "Valor no valido")
    
    def test_interfaz_factorial_78(self):
        result = factorial_interfaz("7.8")
        self.assertEqual(result, "Valor no valido")
    
    def test_interfaz_factorial_62(self):
        result = factorial_interfaz("6,2")
        self.assertEqual(result, "Valor no valido")

if __name__ == '__main__':
   unittest.main()