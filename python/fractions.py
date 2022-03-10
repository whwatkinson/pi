class IncorrectValue(ValueError):
    def __init__(self, value):
        self.message = f"{value} has to be an integer"
        super().__init__(self.message)


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        self.numerator = self.value_check(numerator)
        self.denominator = self.value_check(denominator)

    @staticmethod
    def value_check(value: int) -> int:

        if type(value) != int:
            raise IncorrectValue(value)

        return value

    def __mul__(self, other) -> None:
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator

    def __truediv__(self, other) -> None:
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def normalise(self):
        pass

    @property
    def value(self):
        return round(self.numerator / self.denominator, 5)
