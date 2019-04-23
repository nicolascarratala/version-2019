import unittest
from codif import cod 

class test_codif(unittest.TestCase):

    def test_codif_1 (self):
        code = cod('philipp', 'con')
        self.assertEqual('rvvnwcr', code)

    def test_codif_2 (self):
        code = cod('wikihowisthebest', 'lime')
        self.assertEqual('hqwmswimdbtimmex', code)


if __name__ == '__main__':
   unittest.main()