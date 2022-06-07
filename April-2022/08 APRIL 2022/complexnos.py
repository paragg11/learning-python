import math


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    @property
    def imaginary(self):
        return self.imag

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.imag)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        if isinstance(other, ComplexNumber):
            return other - self
        if isinstance(other, int):
            return ComplexNumber(other.real - self.real, other.imag - self.imag)

    def __truediv__(self, other):
        numer = abs(other) ** 2
        return ComplexNumber((self.real * other.real + self.imag * other.imag) / numer,
                             (self.imag * other.real - self.real * other.imag) / numer)

    def __rtruediv__(self, other):
        if isinstance(other, ComplexNumber):
            return other / self
        if isinstance(other, int):
            numer = int(abs(self) ** 2)
            return ComplexNumber(other.real * self.real / numer,
                                 - other.real * self.imag / numer)

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def exp(self):
        ea = math.exp(1) ** self.real
        return ComplexNumber(ea * math.cos(self.imag),
                             ea * math.sin(self.imag))

    def exp(self):
        pass