class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator must not be zero.")

        self.num = num
        self.den = den

    def __str__(self):
        print(f"{self.num}/{self.den}")

    def __add__(self, fraction):
        num1 = self.num * fraction.den
        num2 = fraction.num * self.den
        return Fraction(num1 + num2, fraction.den*self.den)

    def __sub__(self, fraction):
        num1 = self.num * fraction.den
        num2 = fraction.num * self.den
        return Fraction(num1-num2, fraction.den*self.den)

    def inverse(self):
        return Fraction(self.den, self.num)


# Test case
fraction = Fraction(1, 2)
secondFraction = Fraction(1, 4)

fraction.inverse().__str__()
fraction.__add__(secondFraction).__str__()
fraction.__sub__(secondFraction).__str__()
