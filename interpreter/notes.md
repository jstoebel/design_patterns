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