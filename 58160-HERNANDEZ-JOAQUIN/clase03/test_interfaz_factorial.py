import unittest
from interfaz_factorial import interfaz_factorial

class TestInterfazFactorial(unittest.TestCase):

   def test_interfaz_factorial_1(self):
       result = interfaz_factorial(1)
       self.assertEqual(result, 1)

   def test_interfaz_factorial_Hola(self):
       result = interfaz_factorial ('Hola')
       self.assertEqual(result, 'Error, NO INGRESO UN NUMERO')

   def test_interfaz_factorial_5(self):
       result = interfaz_factorial('5')
       self.assertEqual(result, 120)

if __name__ == '__main__':
   unittest.main()