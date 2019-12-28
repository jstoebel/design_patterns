from typing import Union

INTEGER, PLUS, EOF, SPACE = 'INTEGER', 'PLUS', 'EOF', 'SPACE'

class Token(object):
    """
    an abstract class representing all tokens
    Inheriting classes must:
        - define a self.type in their __init__
        - implement a `value` property
    """
    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class OperatorToken(Token):
    def __init__(self, left_value, right_value) -> None:
        self.left_value  = left_value
        self.right_value = right_value

class AddToken(OperatorToken):
    def __init__(self, left_value, right_value) -> None:
        self.type = 'PLUS'
        super().__init__(left_value, right_value)

    @property
    def value(self):
        """
        returns the sum of left_value and right_value
        """
        return self.left_value.value + self.right_value.value

class SubtractToken(OperatorToken):
    def __init__(self, left_value, right_value):
        self.type = 'PLUS'
        super().__init__(left_value, right_value)

    @property
    def value(self):
        return self.left_value.value - self.right_value.value

class IntWrapper(object):
    def __init__(self, value) -> None:
        self.value = value


