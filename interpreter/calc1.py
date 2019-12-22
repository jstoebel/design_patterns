# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, EOF, SPACE = 'INTEGER', 'PLUS', 'EOF', 'SPACE'


class Token(object):
    def __init__(self, type: Literal['INTEGER'], value: str) -> None:
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

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

    def is_integer(self):
        return self.type == INTEGER

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

    def error(self):
        raise InterpreterParseError('Error parsing input')

    def next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            return Token(INTEGER, int(current_char))
        elif current_char == '+':
            return Token(PLUS, current_char)
        elif current_char == ' ':
            return Token(SPACE, current_char)
        else:
            self.error()

    def get_next_token(self):
        token = self.next_token()
        self.pos += 1
        return token

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def eat_integers(self):
        """
        eats integers tokens until a non integer is found. 
        Returns teh resulting integers
        """
        result = ''
        while True:
            # eat tokens until you hit a non integer. Assume its a plus!
            curr_token = self.current_token
            try:
                self.eat(INTEGER)
                result += str(curr_token.value)
            except InterpreterParseError as e:
                return int(''.join(result))

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        left = self.eat_integers()

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(PLUS)

        # we expect the current token to be a single-digit integer
        right = self.eat_integers()

        # after the above call the self.current_token is set to
        # EOF token
        return left + right

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

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()