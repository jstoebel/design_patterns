from typing import Union, List

INTEGER, PLUS, EOF, SPACE, INT_WRAPPER, MINUS = 'INTEGER', 'PLUS', 'EOF', 'SPACE', 'INT_WRAPPER', 'MINUS'

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
    def __init__(self, left_value) -> None:
        self.left_value  = left_value


    @property
    def right_value(self):
        return self._right_value

    @right_value.setter
    def right_value(self, right_value):
        self._right_value = right_value

class AddToken(OperatorToken):
    def __init__(self, left_value) -> None:
        self.type = 'PLUS'
        super().__init__(left_value)

    @property
    def value(self):
        """
        returns the sum of left_value and right_value
        """
        return self.left_value.value + self.right_value.value

class SubtractToken(OperatorToken):
    def __init__(self, left_value):
        self.type = 'MINUS'
        super().__init__(left_value)

    @property
    def value(self):
        return self.left_value.value - self.right_value.value

class IntToken(Token):
    def __init__(self, value: str) -> None:
        self.value = value
        self.type = INTEGER

class IntWrapper(Token):
    def __init__(self, tokens: List[IntToken] ) -> None:
        self.tokens = tokens
        self.type = INT_WRAPPER

    @property
    def value(self) -> int:
        number_strings = [int_token.value for int_token in self.tokens]
        return int(''.join(number_strings))



