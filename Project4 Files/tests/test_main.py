import unittest
import contextlib
import io
from project4 import read_input, process_input, main

sample_file = 'C:\\Users\\qkzmf\\Downloads\\UCI_Courses\\ICS33\\Project4 Files\\sample3.txt'

class testMainModule(unittest.TestCase):
    def test_read_input(self):
        path, num, init = read_input(True)
        self.assertTrue(path == sample_file and num == 1 and init == 'A')

    def test_process_input(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            process_input(True)
            self.assertEqual(output.getvalue(), 'x\n')

    def test_main(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            main(test=True)
            self.assertEqual(output.getvalue(), 'x\n')

if __name__ == '__main__':
    unittest.main()