from fractions import Fraction
from typing import Union


class Term:

    def __init__(self, coefficient: int, power: int = 0):
        self.coefficient = Fraction(coefficient)
        self.power = power
        self.constant = True if self.power == 0 else False

    def __repr__(self):
        return f"{self.coefficient}x^{self.power}"

    def value(self, x: Union[int, float] = 1) -> Fraction:

        return self.coefficient * (x ** self.power)

    def differentiate(self):

        self.coefficient *= self.power
        self.power -= 1

        if self.power == 0:
            self.constant = True

    def integrate(self):

        self.power += 1
        self.coefficient /= self.power

        if self.power == 0:
            self.constant = False


