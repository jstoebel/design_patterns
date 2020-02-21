import re
import app.token as token
from app.ast import AST
from typing import List

class InterpreterParseError(Exception):
    pass

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = -1
        # current token instance
        self.current_token = None
        self.advance_token()
        self.prev_token = None

    def error(self, msg='Error parsing input'):
        raise InterpreterParseError(msg)


    def get_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.

        Gets the next token but doesn't update state.

        offset: a number representing the the number of characters to offset self.pos.
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
        
        try:
            return token.token_factory(current_char)
        except token.IllegalTokenError:
            self.error()

    def next_non_space(self) -> token.Token:
        """
        return the next non white space character
        """
        remaining_text_stripped = self.text[self.pos:].replace(' ', '')
        if len(remaining_text_stripped):
            return token.token_factory(remaining_text_stripped[0])
        else:
            return token.EOFToken()

    def advance_token(self):
        """
        advances to the next character in the text
        updates state for
            - pos
            - prev_tokenc
            - current_token
        """

        self.pos += 1
        next_token = self.get_token()
        self.prev_token = self.current_token
        self.current_token = next_token

    def done(self):
        return self.current_token.is_a(token.EOF)

    def eat(self, *token_types):
        """
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token, and the current token to self.prev_token
        otherwise raise an exception.
        """

        if self.current_token.type in token_types:
            self.advance_token()
        else:
            self.error()

    def eat_integers(self) -> token.IntWrapper:
        """
        eats integers tokens until a non integer is found. 
        Returns IntWrapper
        """
        tokens = []
        while True:
            # eat tokens until you hit a non integer. Assume its an operator!
            curr_token = self.current_token
            try:
                self.eat(token.INTEGER)
                tokens.append(curr_token)
            except InterpreterParseError as e:
                # the token isn't an integer. If its a space and the next character is an integer too, that's a corner case we need to account for
                if curr_token.is_a(token.SPACE) and self.next_non_space().is_a(token.INTEGER):
                    self.error('illegal space detected')
                return token.IntWrapper(tokens)
    
    def eat_operator(self) -> token.OperatorToken:
        """
        eats the next character expecting it to be an operator
        """
        self.eat(*token.TOKENS)
        return self.prev_token

    def expr(self):
        ast = AST()

        while not self.done():
            if self.current_token.is_operator():
                ast.feed(self.eat_operator())
            elif self.current_token.is_a(token.SPACE):
                self.advance_token()
            else:
                ast.feed(self.eat_integers())

        return ast.value
