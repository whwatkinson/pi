from contextlib import contextmanager
from typing import Union

from pytest import mark, raises

from python.fractions import Fraction, IncorrectValue


@contextmanager
def does_not_raise():
    yield


class TestFraction:
    @mark.parametrize(
        "test_numerator, test_denominator, expected_value, exception",
        [(1, 2, 0.5, does_not_raise()), (1.1, 2, 0.5, raises(IncorrectValue))],
    )
    def test_fraction(
        self,
        test_numerator: int,
        test_denominator: int,
        expected_value: Union[float, int],
        exception,
    ):

        with exception:

            test = Fraction(test_numerator, test_denominator)

            assert test.value == expected_value

    def test_multiply(self):
        pass

    def test_divide(self):
        pass

    def test_normalise(self):
        pass
