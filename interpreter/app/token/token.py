from typing import Union, List

from app.exceptions import FullOperatorError

INTEGER, PLUS, EOF, SPACE, INT_WRAPPER, MINUS, MULTIPLY, DIVIDE = 'INTEGER', 'PLUS', 'EOF', 'SPACE', 'INT_WRAPPER', 'MINUS', 'MULTIPLY', 'DIVIDE'

TOKENS = [PLUS, MINUS, MULTIPLY, DIVIDE]

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

    def higher_in_tree(self, other):
        raise NotImplementedError

    def is_a(self, *args) -> bool:
        """
        Returns if token is of the same type as `type`
        Example:
            token.is_a('INTEGER')
        """
        return any([self.type == type for type in args])


    def is_operator(self) -> bool:
        return False

class SpaceToken(Token):
    def __init__(self) -> None:
        self.type = SPACE
        self.value = None

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

    def feed(self, token):
        """
        Feed a token to this operator. Add token to left_value if its blank.
        If not, add to right_value.
        """
        if self.left_value is None:
            self.left_value = token
        elif self.right_value is None:
            self.right_value = token
        else:
            raise FullOperatorError('Tried to feed a value to a full operator')

    def is_operator(self) -> bool:
        return True

    def bump(self, token):
        """
        operator replaces right_value with token. Token operator's previous right_value
        """
        bumped = self.right_value
        self.right_value = token
        token.feed(bumped)

class AddToken(OperatorToken):
    def __init__(self) -> None:
        self.type = 'PLUS'
        super().__init__()

    def higher_in_tree(self, other):
        if other.is_a('PLUS', 'MINUS'): return False
        return True

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

    def higher_in_tree(self, other):
        if other.is_a('PLUS', 'MINUS'): return False
        return True

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

    def higher_in_tree(self, other):
        if other.is_a('INT_WRAPPER'): return True
        return False

class DivideToken(OperatorToken):
    def __init__(self):
        self.type = 'DIVIDE'
        super().__init__()

    @property
    def value(self):
        return self.left_value.value / self.right_value.value

    def higher_in_tree(self, other):
        if other.is_a('INT_WRAPPER'): return True
        return False
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

    def higher_in_tree(self, other):
        return False

class EOFToken(Token):
    def __init__(self):
        self.type = EOF
        self.value = None