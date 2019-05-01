import unittest
from interfaz import (minor_to_zero,factorial_interface)

class Main (unittest.TestCase):

    def test_minor_to_zero_pass(self):
        a=minor_to_zero(10)
        self.assertEqual(a,10)
    def test_minor_to_zero_error(self):
        a=minor_to_zero(-1)
        self.assertEqual(a,'ERROR')
    def test_factorial_interface_pass(self):
        a=factorial_interface(10)
        self.assertEqual(a,3628800)
    def test_factorial_interface_error(self):
        a=factorial_interface("test")
        self.assertEqual(a,'ERROR')

if __name__ == "__main__":
    unittest.main()