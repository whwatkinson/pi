from typing import Union

from python.fractions import Fraction

"""https://docs.python.org/3/library/decimal.html"""
"""https://pythonhosted.org/bigfloat/"""


class Term:
    def __init__(self, coefficient: int, power: int = 0):
        self.coefficient = Fraction(coefficient)
        self.power = Fraction(power)
        self.constant = True if self.power == 0 else False

    def __repr__(self):
        return f"{self.coefficient}x^{self.power}"

    def value(self, x: Union[int, float] = 1) -> Fraction:
        return self.coefficient * (x**self.power)

    def differentiate(self):

        # bring down the power
        self.coefficient *= self.power
        # Decrease the  power by one
        self.power -= 1

        if self.power == 0:
            self.constant = True

    def integrate(self):

        # Increase the power by one
        self.power += 1
        # Divide by the new power
        self.coefficient /= self.power

        if self.power == 0:
            self.constant = False
