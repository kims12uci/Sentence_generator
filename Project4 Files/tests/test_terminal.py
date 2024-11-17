import unittest
from terminal_class import terminal

class testTerminal(unittest.TestCase):
    def test_creation(self):
        t = terminal('hi')
        self.assertEqual(t.val, 'hi')

    def test_convert(self):
        t = terminal('hi')
        self.assertEqual(list(t.convert()), ['hi'])

if __name__ == '__main__':
    unittest.main()