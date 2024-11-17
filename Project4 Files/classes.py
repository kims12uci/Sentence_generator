import terminal_class as tc
import random


class variable:
    """
    class representing variable symbol.
    Attributes:
        name: the symbol's name.
    Dunder methods:
        init, hash, eq
    Other methods:
        convert
    """
    def __init__(self, name):
        """
        method initializing the object's name.
        Attributes:
            name: the object's name.
        """
        self.name = name

    def __hash__(self):
        """
        method for hash value of the object.
        Returns:
            hash value of the object's name.
        """
        return hash(self.name)

    def __eq__(self, other):
        """
        method for determining equal objects.
        Returns:
            True if other is variable object with same name.
            False otherwise.
        """
        if isinstance(other, variable):
            if self.name == other.name:
                return True
        return False
    def convert(self, gram):
        """
        method called to convert its value, either to another variable or terminal object.
        yields string version of what the variable's rule yields.
        """
        var_rule = gram.get_rule(self)
        yield ''.join(list(var_rule.convert_var(gram)))


class option:
    """
    class representing an option for a variable.
    Attributes:
        weight: relative likelihood for the option to be chosen.
        content: list containing terminal and/or variable objects. default is empty list.
    Dunder methods:
        init
    Other methods:
        convert, add_content
    """
    def __init__(self, weight, content: list[tc.terminal, variable]=None):
        """
        method initializing the object's attributes.
        Attributes:
            weight: relative likelihood for the option to be chosen.
            content: list containing terminal and/or variable objects. default is empty list.
        """
        self.weight = weight
        if content is None:
            self.content = []
        else:
            self.content = content

    def convert(self, gram):
        """
        method called to convert a variable, according to the option's content.
        yields string version of what each object in content yields.
        """
        for item in self.content:
            if isinstance(item, variable):
                yield ''.join(list(item.convert(gram)))
            else:
                yield ''.join(list(item.convert()))

    def add_content(self, cont):
        """
        method to add variable and/or terminal object to the content.
        appends given object to the option's content.
        """
        self.content.append(cont)


class rule:
    """
    class representing a rule for a variable.
    Attributes:
        var: a variable object.
        options: a list of options for the variable. default is an empty list.
    Dunder methods:
        init
    Other methods:
        convert_var, add_option
    """
    def __init__(self, var: variable, options: list[option]=None):
        """
        method initializing the object's attributes.
        Attributes:
            var: a variable object.
            options: a list of options for the variable. default is an empty list.
                     if not default, each option is added to the list equal to its weight.
        """
        self.var = var
        self.options = []
        if options is not None:
            for opt in options:
                for _ in range(opt.weight):
                    self.options.append(opt)

    def convert_var(self, gram):
        """
        method called to convert a variable.
        randomly selects among options corresponding to the variable, then
            yields string version of what the option yields.
        """
        opt = self.options[random.randint(0, len(self.options) - 1)]
        yield ' '.join(list(opt.convert(gram)))

    def add_option(self, opt: option):
        """
        method called to add an option to the rule.
        given option is added to the object's options attribute equal to the option's weight.
        """
        for _ in range(opt.weight):
            self.options.append(opt)


class grammar:
    """
    class representing a grammar.
    Attributes:
        rules: a list of all the rules of the grammar. default is an empty list.
    Dunder methods:
        init
    Other methods:
        create_sentence, get_rule, add_rule
    """
    def __init__(self, rules: list[rule]=None):
        """
        method initializing the object's attributes.
        Attributes:
            rules: a list of all the rules of the grammar. default is an empty list.
        """
        if rules is None:
            self.rules = []
        else:
            self.rules = rules

    def create_sentence(self, sent_num: int, init_var: str):
        """
        method called to create one or more sentence according to the grammar.
        Parameters:
            sent_num: number of times to generate sentences.
            init_var: starting variable.
        prints string version of generated sentences, each sentence ending with a newline.
        """
        init_var = variable(init_var)
        for _ in range(sent_num):
            sentence = ''.join(list(init_var.convert(self)))
            print(sentence)

    def get_rule(self, var: variable):
        """
        method called to find corresponding rule to a given variable.
        Parameters:
            var: a variable object.
        Returns:
            a rule corresponding to the variable.
        """
        for one_rule in self.rules:
            if one_rule.var == var:
                return one_rule

    def add_rule(self, one_rule: rule):
        """
        method called to add a rule to the grammar object.
        adds given rule to its rules attribute.
        """
        self.rules.append(one_rule)