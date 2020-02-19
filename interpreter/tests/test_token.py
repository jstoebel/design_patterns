import pytest
from app.token import *

class TestAddToken:
    def test_add_two_numbers(self):
        left = int_wrapper_factory('10')
        right = int_wrapper_factory('20')

        add = AddToken()

        add.left_value = left
        add.right_value = right
        assert add.value == 30

    def test_add_number_and_sum(self):
        inner_add = AddToken()
        inner_add.left_value = int_wrapper_factory('3')

        inner_add.right_value = int_wrapper_factory('2')

        num = int_wrapper_factory('1')

        outer_add = AddToken()

        outer_add.left_value = inner_add
        outer_add.right_value = num

        assert outer_add.value == 6

    def test_type(self):
        add = AddToken()
        assert add.type == PLUS

class TestSubtractToken:
    def test_subtract_two_numbers(self):
        left = int_wrapper_factory('20')

        right = int_wrapper_factory('11')

        sub = SubtractToken()
        sub.left_value = left

        sub.right_value = right
        assert sub.value == 9

    def test_subtract_number_and_difference(self):
        left = int_wrapper_factory('20')

        sub1 = SubtractToken()

        sub1.left_value = int_wrapper_factory('8')

        sub1.right_value = int_wrapper_factory('3')

        sub2 = SubtractToken()

        sub2.left_value = left

        sub2.right_value = sub1

        assert sub2.value == 15

    def test_type(self):
        sub = SubtractToken()
        assert sub.type == MINUS

class TestIntWrapper:
    def test_value(self):
        num = int_wrapper_factory('10')

        assert num.value == 10

    def test_type(self):
        num = int_wrapper_factory('10')

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