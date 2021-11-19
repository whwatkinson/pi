from pytest import mark

from terms import Term


class TestTerm:

    @mark.parametrize(
        "coefficient, power, expected",
        [
            (1, 1, "1x^1")
        ]
    )
    def test_term_creation(self, coefficient, power, expected):
        test = Term(coefficient, power)
        assert test.coefficient == coefficient
        assert test.power == power
        assert str(test) == expected

    @mark.parametrize(
        "coefficient, power, expected_str, expected_value",
        [
            (2, 2, "4x^1", 4),
            (4, 1, "4x^0", 4),
            (4, 3, "12x^2", 12),
            (1, 1, "1x^0", 1),
            (-2, 2, "-4x^1", -4),
            (2, -2, "-4x^-3", -4),
            (-4, -3, "12x^-4", 12)
        ]
    )
    def test_differentiate(self, coefficient, power, expected_str, expected_value):
        test = Term(coefficient, power)

        test.differentiate()
        assert str(test) == expected_str
        assert test.value(1) == expected_value
