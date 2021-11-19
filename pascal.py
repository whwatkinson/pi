from math import factorial


class Pascal:

    def __init__(self, row_number):
        self.row_number = row_number
        self.row = self.pascals_triangle(row_number)

    @staticmethod
    def combination(n: int, r: int) -> int:
        return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))

    @classmethod
    def pascals_triangle(cls, rows: int):
        result = []
        for n in range(rows):
            row = []
            for r in range(n + 1):

                row.append(cls.combination(n, r))
            result.append(row)

        return result[rows - 1]