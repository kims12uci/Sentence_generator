import unittest
from read_grammar import read_Gram, getContent, take_grammar, make_grammar_class

sample = ['{\n', 'A\n', '1 Boo is [Adj] today\n', '}\n', '\n', 'comment\n', '{\n', 'Adj\n', '3 happy\n', '3 perfect\n', '}']
sample_file = 'C:\\Users\\qkzmf\\Downloads\\UCI_Courses\\ICS33\\Project4 Files\\sample.txt'
sample_gram = [[['{'], ['A'], ['1', 'Boo', 'is', '[Adj]', 'today'], ['}']], [['{'], ['Adj'], ['3', 'happy'], ['3', 'perfect'], ['}']]]

class testReadGrammar(unittest.TestCase):
    def test_get_content_ful_path(self):
        line = getContent(sample_file)
        self.assertEqual(line, sample)

    def test_get_content_current_directory(self):
        line = getContent('sample.txt')
        self.assertEqual(line, sample)

    def test_take_grammar(self):
        gram = take_grammar(sample)
        self.assertEqual(gram, sample_gram)

    def test_make_grammar_class(self):
        gram_class = make_grammar_class(sample_gram)
        self.assertEqual(len(gram_class.rules), 2)

    def test_read_gram(self):
        gram_class = read_Gram(sample_file)
        self.assertEqual(len(gram_class.rules), 2)

if __name__ == '__main__':
    unittest.main()