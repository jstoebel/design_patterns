import pytest
from interpreter.token import AddToken, IntWrapper, SubtractToken


class TestAddToken:
    def test_add_two_numbers(self):
        left = IntWrapper(1)
        right = IntWrapper(2)
        add = AddToken(left, right)
        assert add.value == 3

    def test_add_number_and_sum(self):
        left = AddToken(
            IntWrapper(1),
            IntWrapper(2)
        )

        right = IntWrapper(3)

        add = AddToken(left, right)

        assert add.value == 6

class TestSubtractToken:
    def test_subtract_two_numbers(self):
        left = IntWrapper(3)
        right = IntWrapper(2)
        sub = SubtractToken(left, right)
        assert sub.value == 1

    def test_subtract_number_and_sum(self):
        left = AddToken(
            IntWrapper(2),
            IntWrapper(3)
        )

        right = IntWrapper(1)

        sub = SubtractToken(left, right)

        assert sub.value == 4

class TestIntWrapper:
    def test_returns_wrapped_value(self):
        num = IntWrapper(2)
        assert num.value == 2