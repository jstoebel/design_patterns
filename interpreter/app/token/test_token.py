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
        add = AddToken()

        add.left_value = left
        add.right_value = right
        assert add.value == 30

    def test_add_number_and_sum(self):
        inner_add = AddToken()
        inner_add.left_value = IntWrapper([IntToken('3')])

        inner_add.right_value = IntWrapper([IntToken('2')])

        num = IntWrapper([IntToken('1')])

        outer_add = AddToken()

        outer_add.left_value = inner_add
        outer_add.right_value = num

        assert outer_add.value == 6

    def test_type(self):
        add = AddToken()
        assert add.type == PLUS

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
        sub = SubtractToken()
        sub.left_value = left

        sub.right_value = right
        assert sub.value == 9

    def test_subtract_number_and_difference(self):
        left = IntWrapper([
            IntToken('2'),
            IntToken('0')
        ])
        sub1 = SubtractToken()

        sub1.left_value = IntWrapper([
            IntToken('8'),
        ])

        sub1.right_value = IntWrapper([
            IntToken('3'),
        ])

        sub2 = SubtractToken()

        sub2.left_value = left

        sub2.right_value = sub1

        assert sub2.value == 15

    def test_type(self):
        sub = SubtractToken()
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