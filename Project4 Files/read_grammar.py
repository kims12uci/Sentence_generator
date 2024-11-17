from pathlib import Path
from classes import variable, option, rule, grammar, tc

def read_Gram(path):
    """
    calls different functions in the module to create grammar class
        with the information in the given file.
    Parameter:
        path: path to the file which grammar is written.
    calls:
        getContent, take_grammar, make_grammar_class.
    Returns:
        grammar class object.
    """
    content = getContent(path)
    grammars = take_grammar(content)
    gram_class = make_grammar_class(grammars)
    return gram_class

def getContent(p):
    """
    given path to a grammar file, read it and return the file's content
    Parameter:
        p: path to the grammar file.
    Returns:
        a list with each element as string version of one line of the file.
    """
    path = Path(p)
    if not Path.is_file(path):
        #could not achieve full coverage, as I failed to make this condition false.
        path = Path('./' + p)

    with open(path, 'r') as gram_file:
        lines = gram_file.readlines()

    return lines

def take_grammar(content):
    """
    given a list of lines, filter out non-grammar information.
    Parameter:
        content: an iterable object containing each element as a single line of grammar file.
    Returns:
        a list of lists, with inner lists each containing one rule of the grammar.
        each element in the inner lists are lists with each of them containing one line of the file's content,
            separated by space.
    """
    read = False
    grammars = []
    for line in content:
        line = line.split()
        if len(line):
            if line[0] == '{':
                read = True
                gram = []

            if read:
                gram.append(line)

            if line[0] == '}':
                grammars.append(gram)
                read = False
    return grammars

def make_grammar_class(grammars):
    """
    given a list of rules, construct a grammar class object.
    Parameters:
        grammars: a list of lists, with each inner list containing a rule.
    Returns:
        a grammar class object, containing all the rules, options, variable, and terminals.
    """
    gram_class = grammar()
    for gram in grammars:
        one_var = variable(gram[1][0])
        one_rule = rule(one_var)
        for options in gram[2:-1]:
            one_option = option(int(options[0]))
            for content in options[1:]:
                if '[' in content:
                    one_content = variable(content[1:-1])
                else:
                    one_content = tc.terminal(content)
                one_option.add_content(one_content)
            one_rule.add_option(one_option)
        gram_class.add_rule(one_rule)

    return gram_class