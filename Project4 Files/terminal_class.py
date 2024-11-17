class terminal:
    """
    class representing terminal symbol.
    Attributes:
        val: the symbol's value.
    """
    def __init__(self, val):
        """
        method initializing the object's value.
        Attributes:
            val: the object's value.
        """
        self.val = val

    def convert(self):
        """
        method called to convert its value.
        as terminal symbol, the object simply yields its value.
        """
        yield self.val