import unittest
from pipe_fixer import pipe_fix

class TestPipe_Fixer(unittest.TestCase):
    def test_pipe_fixer_list(self):
        pipe_list=pipe_fix([1,2,3,5,6,8,9])
        self.assertEqual(pipe_list,[1,2,3,4,5,6,7,8,9])
    def test_pipe_fixer_list1(self):
        pipe_list=pipe_fix([1,2,3,12])
        self.assertEqual(pipe_list,[1,2,3,4,5,6,7,8,9,10,11,12])
    def test_pipe_fixer_list2(self):
        pipe_list=pipe_fix([6,9])
        self.assertEqual(pipe_list,[6,7,8,9])
    def test_pipe_fixer_list3(self):
        pipe_list=pipe_fix([-1,4])
        self.assertEqual(pipe_list,[-1,0,1,2,3,4])
    def test_pipe_fixer_list4(self):
        pipe_list=pipe_fix([1,2,3])
        self.assertEqual(pipe_list,[1,2,3])

if __name__ == '__main__':
    unittest.main()