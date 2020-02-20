from app.ast import AST
from app.token import int_wrapper_factory, AddToken, SubtractToken, OperatorToken

class TestAST:
    def test_ast(self):
        ast = AST()
        ast.feed(
            int_wrapper_factory('3')
        )

        ast.feed(AddToken())

        ast.feed(
            int_wrapper_factory('2')
        )

        assert ast.value == 5

    def test_ast_multiple_operators(self):
        ast = AST()
        ast.feed(
            int_wrapper_factory('3')
        )

        ast.feed(AddToken())

        ast.feed(
            int_wrapper_factory('5')
        )

        ast.feed(SubtractToken())

        ast.feed(
            int_wrapper_factory('2')
        )

        assert ast.value == 6