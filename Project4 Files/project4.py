# project4.py
#
# ICS 33 Spring 2023
# Project 4: Still Looking for Something
import read_grammar as rg

def read_input(test):
    """
    take grammar file path, sentence number, and start variable as user input.
    Parameter:
        test: bool object indicating if the run is for unittest.
    Returns:
        path: path to the grammar file.
             for test run, fixed file path is used.
        sent_num: number of sentences to generate from given grammar.
             for test run, fixed to 1.
        s_var: starting variable.
             for test run, fixed to string 'A'
    """
    if test:
        path = 'C:\\Users\\qkzmf\\Downloads\\UCI_Courses\\ICS33\\Project4 Files\\sample3.txt'
        sent_num = 1
        s_var = 'A'
    else:
        # could not test lines where user input is required.
        path = input()
        sent_num = int(input())
        s_var = input()

    return path, sent_num, s_var

def process_input(test):
    """
    calls other functions to actually run the program.
    Parameter:
        test: bool object indicating if the run is for unittest.
    Function calls:
        read_input, rg.read_Gram
    Method calls:
        create_sentence of grammar class
    """
    path, sent_num, s_var = read_input(test)
    gram_class = rg.read_Gram(path)
    gram_class.create_sentence(sent_num, s_var)

def main(*, test=False) -> None:
    """
    the function run when the module is run.
    Parameter:
        test: keyword only argument indicating if the run is for unittest. default is False.
    calls:
        process_input
    """
    process_input(test)


if __name__ == '__main__':
    main()
