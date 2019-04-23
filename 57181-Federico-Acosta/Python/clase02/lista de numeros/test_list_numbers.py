import unittest
from list_numbers import find_max


class TestNumbersFinder(unittest.TestCase):
    def test_find_max_simple_list(self):
       max_number = find_max([1, 2, 3, 4])
       print(max_number)
       self.assertEqual(max_number, 4)

    def test_find_max_simple_unorder_list(self):
       max_number = find_max([4, 1, 2, 3])
       print(max_number)
       self.assertEqual(max_number, 4)

    def test_find_max_simple_with_similars_list(self):
       max_number = find_max([8, 8, 8, 8])
       print(max_number)
       self.assertEqual(max_number, 8)

    def test_find_max_list_with_zero(self):
       max_number = find_max([0])
       print(max_number)
       self.assertEqual(max_number, 0)

    def test_find_max_empty_list(self):
       max_number = find_max([])
       print(max_number)
       self.assertIsNone(max_number)

    def test_max_ugly(self):
        try:
            find_max(1234)
            self.fail()
        except Exception:
            pass
    
    def test_nolist(self):
        max_number = find_max(1234)
        print(max_number)
        self.assertEqual(max_number, "not a number")

    def test_letra(self):
        max_number = find_max([1, 2, "h"])
        print(max_number)
        self.assertEqual(max_number, "contiene letra")


if __name__ == '__main__':
   unittest.main()