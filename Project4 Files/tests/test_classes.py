from classes import variable, option, rule, grammar
from terminal_class import terminal
import unittest
import contextlib
import io

class testVariable(unittest.TestCase):
    def test_creation(self):
        v = variable('hi')
        self.assertEqual(v.name, 'hi')

    def test_hash(self):
        v = variable('hi')
        self.assertEqual(hash(v), hash('hi'))

    def test_eq_true(self):
        v1 = variable('hi')
        v2 = variable('hi')
        self.assertEqual(v1, v2)

    def test_eq_false(self):
        v1 = variable('hi')
        v2 = variable('hello')
        self.assertNotEqual(v1, v2)

    def test_eq_false_type(self):
        v = variable('hi')
        self.assertNotEqual(v, 1)

class testOption(unittest.TestCase):
    def test_creation_default(self):
        o = option(1)
        self.assertEqual(o.weight, 1)

    def test_creation_with_content(self):
        o = option(1, [terminal('a'), terminal('b')])
        self.assertEqual(len(o.content), 2)

    def test_add_content(self):
        o = option(1)
        o.add_content(terminal('a'))
        self.assertEqual(len(o.content), 1)

class testRule(unittest.TestCase):
    def test_creation_default(self):
        v = variable('hi')
        r = rule(v)
        self.assertEqual(r.var, v)

    def test_creation_with_option(self):
        v = variable('hi')
        o = option(1)
        r = rule(v, [o])
        self.assertEqual(len(r.options), 1)

    def test_add_option(self):
        v = variable('hi')
        o = option(1)
        r = rule(v)
        r.add_option(o)
        self.assertEqual(len(r.options), 1)

class testGrammar(unittest.TestCase):
    def test_creation_default(self):
        g = grammar()
        self.assertEqual(g.rules, [])

    def test_creation_with_rule(self):
        v = variable('hi')
        r = rule(v)
        g = grammar([r])
        self.assertEqual(len(g.rules), 1)

    def test_add_rule(self):
        v = variable('hi')
        r = rule(v)
        g = grammar()
        g.add_rule(r)
        self.assertEqual(len(g.rules), 1)

    def test_get_rule(self):
        v = variable('hi')
        r = rule(v)
        g = grammar([r])
        self.assertEqual(g.get_rule(v).var, r.var)

    def test_get_rule_not_found(self):
        v1 = variable('hi')
        v2 = variable('hello')
        r = rule(v1)
        g = grammar([r])
        self.assertEqual(g.get_rule(v2), None)

class testConverts(unittest.TestCase):
    def test_convert_option_only_terminal(self):
        g = grammar()
        o = option(1, [terminal('hi')])
        self.assertEqual(list(o.convert(g)), ['hi'])

    def test_convert_rule(self):
        g = grammar()
        o = option(1, [terminal('hi')])
        v = variable('hi')
        r = rule(v, [o])
        self.assertEqual(list(r.convert_var(g)), ['hi'])

    def test_create_sentence(self):
        v = variable('hi')
        o = option(1, [terminal('hi')])
        r = rule(v, [o])
        g = grammar([r])
        with contextlib.redirect_stdout(io.StringIO()) as output:
            g.create_sentence(1, 'hi')
            self.assertEqual(output.getvalue(), 'hi\n')

    def test_create_sentence_variable_options(self):
        v1 = variable('hi')
        v2 = variable('hello')
        o1 = option(1, [v2])
        o2 = option(1, [terminal('hi')])
        r1 = rule(v1, [o1])
        r2 = rule(v2, [o2])
        g = grammar([r1, r2])
        with contextlib.redirect_stdout(io.StringIO()) as output:
            g.create_sentence(1, 'hi')
            self.assertEqual(output.getvalue(), 'hi\n')


if __name__ == '__main__':
    unittest.main()