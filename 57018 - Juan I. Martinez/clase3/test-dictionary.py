import unittest
from count_letters import count_letters


class TestLetterCounter(unittest.TestCase):
    def test_count_(self):
        result = count_letters('hello world')
        self.assertEqual(result, {
            ' ': 1,
            'e': 1,
            'd': 1,
            'h': 1,
            'l': 3, 
            'o': 2,
            'r': 1,
            'w': 1,
        })

    def test_count_2(self):
        result = count_letters('hola como estas?')
        self.assertEqual(result, {
            ' ': 2,
            'e': 1,
            'h': 1,
            'o': 3,
            'l': 1,
            'a': 2,
            'c': 1,
            'm': 1,
            's': 2,
            't': 1,
            '?': 1,
        })

    def test_count_3(self):
        result = count_letters('Esta funcion, funciona')
        self.assertEqual(result, {
            'E': 1,
            's': 1,
            't': 1,
            'a': 2,
            ' ': 2,
            'f': 2,
            'u': 2,
            'n': 4,
            'c': 2,
            'i': 2,
            'o': 2,
            ',': 1,      
        })

    def test_count_4(self):
        result = count_letters('Esto es un test')
        self.assertEqual(result, {
            'E': 1,
            's': 3, 
            't': 3, 
            'o': 1, 
            ' ': 3, 
            'e': 2, 
            'u': 1, 
            'n': 1       
        })

if __name__ == '__main__':
    unittest.main()