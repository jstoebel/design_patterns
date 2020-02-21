It looks like my extra work in part 1 paid off! The first two problems here were to implement multiplcation and division of two numbrers. This was easy enough!

 - add `*` and `/` to the `strip_text` method
 - add the same characters to the `get_token` method
 - implement `MultiplyToken` and `DivideToken`

Mixing multiplication/division with addition/subtraction will be tricky due to order of operations, but we'll leave that for later

Next, I implemetned a new class called `AST` which is going to handle the logic for how tokens should be arranged

```python
class AST(object):
    def __init__(self):
        self.root = ASTRoot()
        self.current_operator = self.root

    def feed(self, token):
        if token.is_operator():
            self._feed_operator(token)
        else:
            self._feed_number(token)

    def _feed_operator(self, token):
        """
            At the begining of this method the tree will look something like this
            AddOperator
                +
                |
            3<--+-->2

            This method will
            - replace the left_value (in this case 2) with the new operator
            - feed the displaced number to that operator
            - update the current_operator

            At the end of the method, here's how things will look:

                AddOperator
                    +
                    |
                3<--+--->SubtractOperator
                                +
                                |
                            2<--+

        """
        number_to_replace = self.current_operator.right_value
        token.feed(number_to_replace)
        self.current_operator.feed(token)
        self.current_operator = token

    def _feed_number(self, token):
        """
        feed the token to the current_operator (either an operator or AST root)
        """
        self.current_operator.feed(token)

    @property
    def value(self):
        return self.root.value
```

Instances of AST have a method called `feed` which handles the logic of placing new tokens in the tree. At this point, a token can be either a number or operator, and helper methods are implemented for each one. Finally, there is a `value` property which kicks off evaluation.

There is one other wrinkle though that I didn't anticipate at first. At the begining, the first token will be a number, but we've been assuming up to this point at a number token will always be contained inside an operator. That's a correct assumption for a valid expression, but until that first operator comes along, we've violated an invariant of the class. So what do we do? My solution was this: let's refactor operator tokens to use a single method for taking on child tokens: `feed`

```python
    def feed(self, token):
        """
        Feed a token to this operator. Add token to left_value if its blank.
        If not, add to right_value.
        """
        if self.left_value is None:
            self.left_value = token
        else:
            self.right_value = token
```

That's a win because it encapsulates the logic for deciding where a child token goes in an operator. Next, we'll use the null objet pattern, to create an object that can contain that first number. It will also respond to `feed` as well as `right_value`

```python
class ASTRoot(object):
    """
    Root of the AST
    Also acts as a null object, replicating the API of an operator
    """
    def __init__(self):
        self.child = None

    def feed(self, token):
        self.child = token

    @property
    def right_value(self):
        """
        this object doesn't really have a right_value but it needs to replicate the API of operators which do.
        """
        return self.child

    @property
    def value(self):
        if self.child is None: return None
        return self.child.value
```

Great! Now to make use of it in `interpreter`. Here's the new `expr` method

```python
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
```

You'll notice there a few new additions:

 - a method called `done` which checks if the curerent token is `EOF`
 - `is_operator` which returns if the current token is an operator
 - `is_a` which encapsulates checking a token's type. I could use the native `type` + `is` but I wanted something that could give me more control later on.
 - `advance_token` is an evolution from `get_next_token`. It updates the state in the same way, but it doesn't return anything. I was finding that updating state and returning a token we're two seperate concerns and I didn't want to mix them up
 - `eat_token` same idea as `eat_integers`

I also developed a more sophisticated way to handle spaces. I added a new `SpaceToken` and then have the interpreter skip over it. The one corner case to consider is a space between number characters, such as `1 0 + 3`. That's should be a syntax error I think. I'm going to handle that error inside of `eat_integers`

```python
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

                # new code here
                return token.IntWrapper(tokens)
```

Hmmm...how to check for this corner case? If we hit a space character here, it may very well be legal (see: `10 + 3`). The space after `10` is perfectly fine. Really, our problem is if the next, non space character is a number. Here's how I'll detect that.

```python
    def next_non_space(self) -> token.Token:
        """
        return the next non white space character
        """

        # get all of the remaining characters
        # if there are any:
            # return the first one as a token
        # else:
            # return EOF
```

This method will share some of the logic as `next_token`, which is a good indication we should extract the common logic to its own function. I made a new function called `token_factory`

```python
class IllegalTokenError(Exception):
    pass

def token_factory(char: str) -> token.Token:
    if char.isdigit():
        return token.IntToken(char)
    elif char == '+':
        return token.AddToken()
    elif char == '-':
        return token.SubtractToken()
    elif char == '*':
        return token.MultiplyToken()
    elif char == '/':
        return token.DivideToken()
    elif char == ' ':
        return token.SpaceToken()
    else:
        raise IllegalTokenError
```

Now I can implement `next_non_space`

```python
    def next_non_space(self) -> token.Token:
        """
        return the next non white space character
        """
        remaining_text_stripped = self.text[self.pos:].replace(' ', '')
        if len(remaining_text_stripped):
            return token.token_factory(remaining_text_stripped[0])
        else:
            return token.EOFToken()
```

And that enables me to complete error checking in `eat_integers`

```python
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
```

Now the interpreter can handle spaces without having to throw them away at the begining.