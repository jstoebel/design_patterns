import pytest
from interpreter.calc1 import Interpreter, InterpreterParseError

def test_single_digit():
    # test digit plus digit
    interpreter = Interpreter('1+2')
    assert interpreter.expr() == 3

def test_multi_digits():
    # test adding multiple digits
    interpreter = Interpreter('10+20')
    assert interpreter.expr() == 30

def test_syntax_error():
    # test various syntax errors that shouldn't ever work
    bad_strings = [
        ['', ValueError],
        ['1', InterpreterParseError],
        ['1+', ValueError],
        ['+1', ValueError],
        ['+', ValueError]
    ]

    for string, error in  bad_strings:
        print(f"with {string}")
        i = Interpreter(string)
        with pytest.raises(error):
            i.expr()