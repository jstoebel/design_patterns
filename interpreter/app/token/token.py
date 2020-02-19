from typing import Union, List

INTEGER, PLUS, EOF, SPACE, INT_WRAPPER, MINUS, MULTIPLY, DIVIDE = 'INTEGER', 'PLUS', 'EOF', 'SPACE', 'INT_WRAPPER', 'MINUS', 'MULTIPLY', 'DIVIDE'

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
    def __init__(self) -> None:
        __slots__ = 'left_value', 'right_value'
        self.left_value = None
        self.right_value = None

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {left}, {right})'.format(
            type=self.type,
            left=self.left_value,
            right=self.right_value
        )

class AddToken(OperatorToken):
    def __init__(self) -> None:
        self.type = 'PLUS'
        super().__init__()

    @property
    def value(self):
        """
        returns the sum of left_value and right_value
        """
        return self.left_value.value + self.right_value.value

class SubtractToken(OperatorToken):
    def __init__(self):
        self.type = 'MINUS'
        super().__init__()

    @property
    def value(self):
        return self.left_value.value - self.right_value.value

class MultiplyToken(OperatorToken):
    def __init__(self):
        self.type = 'MULTIPLY'
        super().__init__()

    @property
    def value(self):
        return self.left_value.value * self.right_value.value

class DivideToken(OperatorToken):
    def __init__(self):
        self.type = 'DIVIDE'
        super().__init__()

    @property
    def value(self):
        return self.left_value.value / self.right_value.value

class IntToken(Token):
    """
    represents a single numeric character. Example '3'
    """
    def __init__(self, value: str) -> None:
        self.value = value
        self.type = INTEGER

class IntWrapper(Token):
    """
    a list of string of IntTokens that represent an integer.
    """
    def __init__(self, tokens: List[IntToken] ) -> None:
        self.tokens = tokens
        self.type = INT_WRAPPER

    @property
    def value(self) -> int:
        number_strings = [int_token.value for int_token in self.tokens]
        return int(''.join(number_strings))

class EOFToken(Token):
    def __init__(self):
        self.type = EOF
        self.value = None