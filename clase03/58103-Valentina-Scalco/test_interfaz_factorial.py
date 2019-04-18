import unittest
from factorial_interfaz import factorial_interfaz

class TestInterfazFactorial(unittest.TestCase):
   def test_interfaz_factorial_5(self):
       result = factorial_interfaz ('5')
       self.assertEqual(result, 5)

   def test_interfaz_factorial_hola(self):
       result = factorial_interfaz('hola')
       self.assertEqual(result,'Error')


if __name__ == '__main__':
   unittest.main()