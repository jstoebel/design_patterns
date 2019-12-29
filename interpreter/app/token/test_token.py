import pytest
from .token import *

class TestAddToken:
    def test_add_two_numbers(self):
        left = IntWrapper([
            IntToken('1'),
            IntToken('0')
        ])
        right = IntWrapper([
            IntToken('2'),
            IntToken('0')
        ])
        add = AddToken(left)

        add.right_value = right
        assert add.value == 30

    def test_add_number_and_sum(self):
        inner_add = AddToken(IntWrapper([IntToken('3')]))

        inner_add.right_value = IntWrapper([IntToken('2')])

        num = IntWrapper([IntToken('1')])

        outer_add = AddToken(inner_add)

        outer_add.right_value = num
        assert outer_add.value == 6

class TestSubtractToken:
    def test_subtract_two_numbers(self):
        left = IntWrapper([
            IntToken('2'),
            IntToken('0')
        ])
        right = IntWrapper([
            IntToken('1'),
            IntToken('1')
        ])
        sub = SubtractToken(left)

        sub.right_value = right
        assert sub.value == 9

    def test_subtract_number_and_difference(self):
        left = IntWrapper([
            IntToken('2'),
            IntToken('0')
        ])
        add = SubtractToken(IntWrapper([
            IntToken('8'),
        ]))

        add.right_value = IntWrapper([
            IntToken('3'),
        ])

        sub = SubtractToken(left)

        sub.right_value = add

        assert sub.value == 15

    def test_type(self):
        left = IntWrapper([
            IntToken('2'),
            IntToken('0')
        ])
        right = IntWrapper([
            IntToken('1'),
            IntToken('1')
        ])
        sub = SubtractToken(left)

        sub.right_value = right

        assert sub.type == MINUS

class TestIntWrapper:
    def test_value(self):
        num = IntWrapper([
            IntToken('1'),
            IntToken('0')
        ])
        assert num.value == 10

    def test_type(self):
        num = IntWrapper([
            IntToken('1'),
            IntToken('0')
        ])

        assert num.type == INT_WRAPPER

class TestIntToken:

    def test_value(self):
        t = IntToken('3')
        assert t.value == '3'

    def test_type(self):
        t = IntToken('3')
        assert t.type == INTEGER

class TestEOFToken:

    @staticmethod
    def token():
        return EOFToken()

    def test_value(self):
        assert self.token().value == None

    def test_type(self):
        assert self.token().type == EOF