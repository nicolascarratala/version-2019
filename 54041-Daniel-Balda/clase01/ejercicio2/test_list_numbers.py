import unittest
from list_numbers import find_max
from pipe_fixer import pipe_fix

# Number List Max test

class TestNumbersFinder(unittest.TestCase):
    def test_find_max_simple_list(self):
        max_number = find_max([1, 2, 3, 4])
        self.assertEqual(max_number, 4)

    def test_find_max_simple_unorder_list(self):
        max_number = find_max([4, 1, 2, 3])
        self.assertEqual(max_number, 4)

    def test_find_max_simple_with_similars_list(self):
        max_number = find_max([8, 8, 8, 8])
        self.assertEqual(max_number, 8)

    def test_find_max_list_with_zero(self):
        max_number = find_max([0])
        self.assertEqual(max_number, 0)

    def test_find_max_empty_list(self):
        max_number = find_max([])
        self.assertIsNone(max_number)

    def test_find_max_list_is_not_a_list_UGLY_2(self):
        from list_numbers import NotAListException
        from list_numbers import NotAllNumberInListException
        try:
            find_max(1234)
            self.fail()
        except NotAListException:
            pass
        except NotAllNumberInListException:
            self.fail()

    def test_find_max_list_not_all_number_in_list_UGLY(self):
        from list_numbers import NotAListException
        from list_numbers import NotAllNumberInListException
        try:
            find_max([1, 2, 3, 4, 'HOLA'])
            self.fail()
        except NotAListException:
            self.fail()
            print ("Ingresa un numero pelotudo")
        except NotAllNumberInListException:
            pass

    # Pipe fixer Test

class TestPipeFixing(unittest.TestCase):
   def test_fix_simple_pipe(self):
       fixed_pipe = pipe_fix([1, 2, 3, 5, 6, 8, 9])
       self.assertEqual(
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           fixed_pipe,
       )

   def test_fix_complex_pipe(self):
       fixed_pipe = pipe_fix([1, 2, 3, 12])
       self.assertEqual(
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
           fixed_pipe,
       )

   def test_fix_short_from_6_pipe(self):
       fixed_pipe = pipe_fix([6, 9])
       self.assertEqual(
           [6, 7, 8, 9],
           fixed_pipe,
       )

   def test_fix_simple_and_negative_pipe(self):
       fixed_pipe = pipe_fix([-1, 4])
       self.assertEqual(
           [-1, 0, 1, 2, 3, 4],
           fixed_pipe,
       )

   def test_fix_already_fixed_pipe(self):
       fixed_pipe = pipe_fix([1, 2, 3])
       self.assertEqual(
           [1, 2, 3],
           fixed_pipe,
       )

if __name__ == '__main__':
    unittest.main()