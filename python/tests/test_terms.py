from fractions import Fraction

from pytest import mark

from python.terms import Term


class TestTerm:
    @mark.parametrize(
        "coefficient, power, expected_str, expected_value", [(1, 1, "1x^1", 1)]
    )
    def test_term_creation(self, coefficient, power, expected_str, expected_value):
        test = Term(coefficient, power)
        assert test.coefficient == coefficient
        assert test.power == power
        assert str(test) == expected_str
        assert test.value(1) == expected_value

    @mark.parametrize(
        "coefficient, power, value, expected_str, expected_value",
        [
            (2, 2, 2, "4x^1", 8),
            (4, 1, 1, "4x^0", 4),
            (4, 3, 3, "12x^2", 108),
            (1, 1, 1, "1x^0", 1),
            (-2, 2, 1, "-4x^1", -4),
            (2, -2, 1, "-4x^-3", -4),
            (-4, -3, 1, "12x^-4", 12),
            (2, 1 / 2, 1, "1x^-1/2", 1),
            (6, 3 / 2, 1, "9x^1/2", 9),
            (2, -3 / 2, 1, "-3x^-5/2", -3),
        ],
    )
    def test_differentiate(
        self, coefficient, power, value, expected_str, expected_value
    ):
        test = Term(coefficient, power)

        test.differentiate()
        assert str(test) == expected_str
        assert test.value(value) == expected_value

    @mark.parametrize(
        "coefficient, power, value, expected_string, expected_value",
        [
            (1, 1, 1, "1/2x^2", Fraction(1, 2)),
            (1, 0, 1, "1x^1", 1),
            (2, 2, 1, "2/3x^3", Fraction(2, 3)),
            (8, 6, 1, "8/7x^7", Fraction(8, 7)),
            (1, 1 / 2, 2, "2/3x^3/2", 1.8856180831641267),
        ],
    )
    def test_integrate(
        self, coefficient, power, value, expected_string, expected_value
    ):

        test = Term(coefficient, power)

        test.integrate()
        assert str(test) == expected_string
        assert test.value(value) == expected_value
