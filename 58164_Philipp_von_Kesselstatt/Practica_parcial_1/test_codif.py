import unittest
from codif import cod 

class test_codif(unittest.TestCase):

    def test_codif_1 (self):
        code = cod('philipp', 'con')
        self.assertEqual('rvvnwcr', code)

    def test_codif_2 (self):
        code = cod('wikihowisthebest', 'lime')
        self.assertEqual('hqwmswimdbtimmex', code)

    def test_codif_3 (self):
        try:
            cod(1, 16)
            self.fail()
        except Exception:
            pass


    def test_codif_4 (self):
        try:
            cod('_', '!')
            self.fail()
        except Exception:
            pass

    def test_codif_5 (self):
        try:
            cod('', '')
            self.fail()
        except Exception:
            pass

if __name__ == '__main__':
   unittest.main()