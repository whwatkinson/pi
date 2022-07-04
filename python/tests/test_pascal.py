from pytest import mark

from python.pascal import Pascal


class TestPascal:
    @mark.parametrize(
        "line_number, expected_result",
        [(0, [1]), (1, [1, 1]), (6, [1, 6, 15, 20, 15, 6, 1])],
    )
    def test_pascal_row(self, line_number, expected_result):

        test = Pascal(line_number)

        assert test.row == expected_result

        assert len(test.row) == line_number + 1

        if line_number > 0:
            assert test.row[1] == line_number
