import app.token as token
from typing import List

class InterpreterParseError(Exception):
    pass

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = self.strip_text(text)
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.prev_token = None

    def error(self):
        raise InterpreterParseError('Error parsing input')

    def next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.

        Gets the next token but doesn't update state.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return token.EOFToken()

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            return token.IntToken(current_char)
        elif current_char == '+':
            return token.AddToken()
        elif current_char == '-':
            return token.SubtractToken()
        else:
            self.error()

    def get_next_token(self):
        token = self.next_token()
        self.pos += 1
        return token

    def eat(self, *token_types):
        """
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token, and the current token to self.prev_token
        otherwise raise an exception.
        """
        if self.current_token.type in token_types:
            self.prev_token = self.current_token
            self.current_token = self.get_next_token()
        else:
            self.error()

    def eat_integers(self) -> token.IntWrapper:
        """
        eats integers tokens until a non integer is found. 
        Return 
        """
        tokens = []
        while True:
            # eat tokens until you hit a non integer. Assume its an operator!
            curr_token = self.current_token
            try:
                self.eat(token.INTEGER)
                tokens.append(curr_token)
            except InterpreterParseError as e:
                return token.IntWrapper(tokens)

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        left = self.eat_integers()

        # we expect the current token to be a '+' or '-' token
        operator = self.current_token
        self.eat(token.PLUS, token.MINUS)

        # we expect the current token to be a single-digit integer
        right = self.eat_integers()

        operator.left_value = left
        operator.right_value = right
        # after the above call the self.current_token is set to
        # EOF token
        return operator.value

    @staticmethod
    def strip_text(text):
        """
        strips valid empty space from expression
        text: expression string
        returns: expression with valid spaces removed
        """
        split_expr = text.split('+')
        stripped = [ char.strip() for char in split_expr]
        return '+'.join(stripped)