import unittest
from factorial import factorial_num

class Main(unittest.TestCase):
    
    def test_fatorial_num_A(self):
        a=factorial_num(10)
        self.assertEqual(a,3628800)

    def test_fatorial_num_B(self):
        a=factorial_num(25)
        self.assertEqual(a,15511210043330985984000000)


if __name__ == "__main__":
    unittest.main()