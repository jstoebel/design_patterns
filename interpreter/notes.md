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
    return '+'.join(stripped) # join expressions together with a pls in the middle
```