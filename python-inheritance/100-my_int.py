"""module that defines Myint inherits from int"""

class Myint(int):
    """Representing Myint class from int"""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value    
