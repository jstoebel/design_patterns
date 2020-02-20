# Part 1

Compiler takes source code and preprocesses it into a machine language.

An interpreter interprets source code without turning it into machine language first. 

Lexical analysis: read input of characters and convert into a stream of tokens.
Token: an object represetning type and value. Example: the token "3" is an integer with value of 3

## exercises

### multiple digits

The assumptions are changing where instead of having digit ->plus->digit we have an arbitrary number of digits followed by a plus followed by an arbitrary number of digits. Let’s write a function that eats tokens keeping track of their values until we hit a non integer. Then return the resulting values parsed as an integer. 

```python
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

```

### spaces

Rather than have the interpreter process spaces, I am going to remove them prior to processing. We can't allow spaces just anywhere however ('1 0 + 3' for example). For a space character to be legal both of its neighboors must be either a space or different from one another. Here's how I'm doing it:

```python
@staticmethod
def strip_text(text):
    """
    strips valid empty space from expression
    text: expression string
    returns: expression with valid spaces removed
    """
    split_expr = text.split('+') # split expression on plus, getting list two expressions.
    stripped = [ char.strip() for char in split_expr] # strip leading and trailing white space
    return '+'.join(stripped) # join expressions together with a plus in the middle
```

### Support addition or subtraction

I may have gone overboard on this one :) I wanted to generalize the concept of an operator which takes two numbers and, using a common interface returns the result. Further, I wanted to be able to construct an AST of operator nodes and integer leaf nodes. All of these nodes respond to `value` which allows for computing an expression by calling `value` on the root and recursivly evaluating each node. Here's what I did.

First I extracted the `Token` class, to keep as my base class

```python
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
```

next I defined an abstract `OperatorToken` which represents any binary operator.

```python
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
```

A general binary operator has a left_value and a right_value. The child class will implement what to do with those two values to determine the result.

Next, we've got two operators, addition and subtraction. Really their only differences are 1) they need to know their `type` and 2) they both need to implement a property `value` which returns either the sum or difference of their two values.

```python
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
```

Next, how to represent numbers. Really there's two different concepts to deal with. The first is an integer token, which is a single digit.

```py
class IntToken(Token):
    """
    represents a single numeric character. Example '3'
    """
    def __init__(self, value: str) -> None:
        self.value = value
        self.type = INTEGER
```

Next is the concept of an entire number, which is composed of one or many digits. Let's think of that as an object which wraps a list of `IntTokens`

```py
class IntWrapper(Token):
    """
    a list of IntTokens that represent an integer.
    """
    def __init__(self, tokens: List[IntToken] ) -> None:
        self.tokens = tokens
        self.type = INT_WRAPPER

    @property
    def value(self) -> int:
        number_strings = [int_token.value for int_token in self.tokens]
        return int(''.join(number_strings))
```

And finally, we have the `EOF` token. Not much to say there

```py
class EOFToken(Token):
    def __init__(self):
        self.type = EOF
        self.value = None
```

The update to `expr` in Interpreter looks like this

```py
def expr(self):
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
```

Finally, I need to update my `strip_text` method to allow subtraction

```py
def strip_text(self, text):
    """
    strips valid empty space from expression
    text: expression string
    returns: expression with valid spaces removed
    """

    try:
        operator = re.search(r'[\+-]', text).group(0) # find the operator, either a + or -
    except(AttributeError):
        raise self.error('expression does not contain an operator') # this error means neither operator was found. Throw our custom exception

    split_expr = text.split(operator)
    stripped = [ char.strip() for char in split_expr]
    return operator.join(stripped)
```


This architecture opens the door for constructing a more complex abstract syntax tree, with any number of binary operators.