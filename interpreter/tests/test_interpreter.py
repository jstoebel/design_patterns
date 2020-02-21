import pytest
from app.interpreter import *

def test_lone_digit():
    assert calc('1') == 1

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

    ('20 - 10', 10),
    (' 20-10', 10),
    ('20-10 ', 10)
])
def test_allows_white_space(string, result):
    # test adding multiple digits
    assert calc(string) == result

def test_subtraction():
    assert calc('10-1') == 9

def test_multiplication():
    assert calc('5*2') == 10

def test_division():
    assert calc('10/2') == 5

@pytest.mark.parametrize('string,result', [
    ('3 + 5 - 2', 6),
    ('7 - 3 + 2 - 1', 5),
    ('10 + 1 + 2 - 3 + 4 + 6 - 15', 5),
])
def test_arbitrary_add_or_subtract(string, result):
    assert calc(string) == result

@pytest.mark.parametrize('string,result', [
    ('7 * 4 / 2 * 3', 42),
    ('10 * 4  * 2 * 3 / 8', 30)
])
def test_arbitrary_multiply_or_divide(string, result):
    assert calc(string) == result

@pytest.mark.parametrize('string,result', [
    ('2 + 7 * 4', 30),
    ('7 - 8 / 4', 5),
    ('14 + 2 * 3 - 6 / 2', 17),
])
def test_add_subtract_multiply_and_divide(string, result):
    assert calc(string) == result

def test_empty_string():
    assert calc('') == None

def test_white_space_only():
    assert calc('   ') == None

bad_inputs = [

    ('1+', AttributeError),
    ('+1', TypeError),
    ('+', AttributeError),
    ('1 0 + 3', InterpreterParseError),

    ('1-', AttributeError),
    ('-1', TypeError),
    ('-', AttributeError),
    ('1 0 - 3', InterpreterParseError),
]

@pytest.mark.parametrize('string,exception', bad_inputs)
def test_syntax_error(string, exception):
    # test various syntax errors that shouldn't ever work

    with pytest.raises(exception):
        calc(string)

def calc(exp):
    interpreter = Interpreter(exp)
    return interpreter.expr()