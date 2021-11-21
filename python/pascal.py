from math import factorial
from typing import List


class Pascal:
    def __init__(self, row_number):
        self.row_number = row_number
        self.row = self.pascals_triangle(row_number)

    @staticmethod
    def combination(n: int, r: int) -> int:
        return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))

    @classmethod
    def pascals_triangle(cls, rows: int) -> List[int]:
        return [cls.combination(rows, r) for r in range(rows + 1)]
