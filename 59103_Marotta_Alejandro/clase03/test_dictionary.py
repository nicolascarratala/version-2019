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
        result = count_letters('hola mundo')
        self.assertEqual(result, {
            ' ': 1,
            'h': 1,
            'o': 2,
            'l': 1,
            'a': 1,
            'm': 1,
            'u': 1,
            'n': 1,
            'd': 1,
        })


if __name__ == '__main__':
    unittest.main()