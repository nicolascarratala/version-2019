import unittest
from pipe_fixer import pipe_fix

class TestPipes(unittest.TestCase):
    def test1(self):
        prueba = pipe_fix([1, 3, 5, 6, 7, 8])
        self.assertEqual(prueba, [1, 2, 3, 4, 5, 6, 7, 8])
    def test2(self):
        prueba = pipe_fix([4])
        self.assertEqual(prueba, [4])
    def test3(self):
        prueba = pipe_fix([2, 5, 9])
        self.assertEqual(prueba, [2, 3, 4, 5, 6, 7, 8, 9])
    def test4(self):
        prueba = pipe_fix([1,9])
        self.assertEqual(prueba, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
   unittest.main()