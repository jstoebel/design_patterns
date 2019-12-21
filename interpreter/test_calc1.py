import pytest
from interpreter.calc1 import Interpreter, InterpreterParseError

def test_single_digit():
    # test digit plus digit
    assert calc('1+2') == 3

def test_multi_digits():
    # test adding multiple digits
    assert calc('10+20') == 30

def test_allows_white_space():
    # test adding multiple digits
    assert calc('10 + 20') == 30

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

def calc(exp):
    interpreter = Interpreter(exp)
    return interpreter.expr()