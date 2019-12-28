import pytest
from interpreter.calc1 import Interpreter, InterpreterParseError

def test_single_digit():
    # test digit plus digit
    assert calc('1+2') == 3

def test_multi_digits():
    # test adding multiple digits
    assert calc('10+20') == 30

@pytest.mark.parametrize('string,result', [
    ('10 + 20', 30),
    (' 10+20', 30),
    ('10+20 ', 30),
])
def test_allows_white_space(string, result):
    # test adding multiple digits
    assert calc(string) == result

def test_subtraction():
    assert calc('10-1') == 9

bad_inputs = [
    ('', ValueError),
    ('1', InterpreterParseError),
    ('1+', ValueError),
    ('+1', ValueError),
    ('+', ValueError),
    ('1 0 + 3', InterpreterParseError),
]

@pytest.mark.parametrize('string,exception', bad_inputs)
def test_syntax_error(string, exception):
    # test various syntax errors that shouldn't ever work


    i = Interpreter(string)
    with pytest.raises(exception):
        i.expr()

def calc(exp):
    interpreter = Interpreter(exp)
    return interpreter.expr()