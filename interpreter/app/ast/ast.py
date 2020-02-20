from app.token import OperatorToken

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
        this object doesn't really have a left_value but it needs to replicate the API of operators which do.
        """
        return self.child

    @property
    def value(self):
        return self.child.value


class AST(object):
    def __init__(self):
        self.root = ASTRoot()
        self.current_operator = self.root

    def feed(self, token):
        if isinstance(token, OperatorToken):
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
