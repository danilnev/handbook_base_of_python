def max_common_divisor(num1, num2):
    if 0 in (num1, num2):
        return 1
    while num1 % num2 != 0 and num2 % num1 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return min([num1, num2])


def min_common_multiply(num1, num2):
    if 0 in (num1, num2):
        return 1
    i = max(num1, num2)
    while True:
        if i % num1 == 0 and i % num2 == 0:
            return i
        i += 1


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            if type(args[0]) == str and len(args[0]) > 1:
                num1, num2 = map(int, list(args[0].split('/')))
            else:
                num1 = int(args[0])
                num2 = 1
        else:
            num1, num2 = args
        if num1 < 0 and num2 < 0:
            _oper = '+'
            num1 = -num1
            num2 = -num2
        elif num1 > 0 and num2 > 0:
            _oper = '+'
        elif num1 < 0:
            _oper = '-'
            num1 = -num1
        elif num2 < 0:
            _oper = '-'
            num2 = -num2
        if 0 in (num1, num2):
            self.numer = 0
            self.denomin = 0
            self._oper = '+'
        else:
            mcd = max_common_divisor(num1, num2)
            if mcd != 0:
                num1 //= mcd
                num2 //= mcd
            self.numer = num1
            self.denomin = num2
            self._oper = _oper

    def numerator(self, *args, not_min=True):
        if len(args) == 0:
            return self.numer
        else:
            number = args[0]
            if number == 0:
                self.numerator(0)
                self.denominator(0)
            else:
                if number < 0:
                    number = -number
                    if self._oper == '+':
                        self._oper = '-'
                    else:
                        self._oper = '+'
                self.numer = number
                if not_min:
                    mcd = max_common_divisor(self.numer, self.denomin)
                    self.numer //= mcd
                    self.denomin //= mcd

    def denominator(self, *args, not_min=True):
        if len(args) == 0:
            return self.denomin
        else:
            number = args[0]
            if number == 0:
                self.numerator(0)
                self.denominator(0)
            else:
                if number < 0:
                    number = -number
                    if self._oper == '+':
                        self._oper = '-'
                    else:
                        self._oper = '+'
                self.denomin = number
                if not_min:
                    mcd = max_common_divisor(self.numer, self.denomin)
                    self.numer //= mcd
                    self.denomin //= mcd

    def __str__(self):
        if self._oper == '+':
            return f'{self.numer}/{self.denomin}'
        else:
            return f'-{self.numer}/{self.denomin}'

    def __repr__(self):
        if self._oper == '+':
            return f'Fraction(\'{self.numer}/{self.denomin}\')'
        else:
            return f'Fraction(\'-{self.numer}/{self.denomin}\')'

    def __neg__(self):
        if self._oper == '+':
            return Fraction(-self.numer, self.denomin)
        else:
            return Fraction(self.numer, self.denomin)

    def __add__(self, others):
        if self._oper == '+':
            frac1 = Fraction(self.numerator(), self.denominator())
        else:
            frac1 = Fraction(-(self.numerator()), self.denominator())
        if type(others) in [int, str]:
            frac2 = Fraction(int(others), 1)
        else:
            if others._oper == '+':
                frac2 = Fraction(others.numerator(), others.denominator())
            else:
                frac2 = Fraction(-(others.numerator()), others.denominator())
        if frac2.numerator() == 0:
            return self
        elif self.numerator() == 0:
            return frac2
        else:
            mcm = min_common_multiply(frac1.denominator(), frac2.denominator())
            count1 = mcm // frac1.denominator()
            count2 = mcm // frac2.denominator()
            frac1.denominator(frac1.denominator() * count1, not_min=False)
            frac2.denominator(frac2.denominator() * count2, not_min=False)
            frac1.numerator(frac1.numerator() * count1, not_min=False)
            frac2.numerator(frac2.numerator() * count2, not_min=False)
            if frac1._oper == frac2._oper == '+':
                return Fraction(frac1.numerator() + frac2.numerator(), frac1.denominator())
            elif frac1._oper == frac2._oper == '-':
                return Fraction(-(frac1.numerator()) + -(frac2.numerator()), frac1.denominator())
            elif frac1._oper == '-':
                return Fraction(-(frac1.numerator()) + frac2.numerator(), frac1.denominator())
            else:
                return Fraction(frac1.numerator() + -(frac2.numerator()), frac1.denominator())

    def __sub__(self, others):
        if self._oper == '+':
            frac1 = Fraction(self.numerator(), self.denominator())
        else:
            frac1 = Fraction(-(self.numerator()), self.denominator())
        if type(others) in [int, str]:
            frac2 = Fraction(int(others), 1)
        else:
            if others._oper == '+':
                frac2 = Fraction(others.numerator(), others.denominator())
            else:
                frac2 = Fraction(-(others.numerator()), others.denominator())
        if frac2.numerator() == 0:
            return self
        elif self.numerator() == 0:
            return -frac2
        else:
            mcm = min_common_multiply(frac1.denominator(), frac2.denominator())
            count1 = mcm // frac1.denominator()
            count2 = mcm // frac2.denominator()
            frac1.denominator(frac1.denominator() * count1, not_min=False)
            frac2.denominator(frac2.denominator() * count2, not_min=False)
            frac1.numerator(frac1.numerator() * count1, not_min=False)
            frac2.numerator(frac2.numerator() * count2, not_min=False)
            if frac1._oper == frac2._oper == '+':
                return Fraction(frac1.numerator() - frac2.numerator(), frac1.denominator())
            elif frac1._oper == frac2._oper == '-':
                return Fraction(-(frac1.numerator()) - -(frac2.numerator()), frac1.denominator())
            elif frac1._oper == '-':
                return Fraction(-frac1.numerator() - frac2.numerator(), frac1.denominator())
            else:
                return Fraction(frac1.numerator() - -(frac2.numerator()), frac1.denominator())

    def __isub__(self, others):
        if type(others) in [int, str]:
            frac2 = Fraction(int(others), 1)
        else:
            if others._oper == '+':
                frac2 = Fraction(others.numerator(), others.denominator())
            else:
                frac2 = Fraction(-(others.numerator()), others.denominator())
        if frac2.numerator() == 0:
            return self
        elif self.numerator() == 0:
            self = -frac2
            return self
        else:
            mcm = min_common_multiply(self.denominator(), frac2.denominator())
            count1 = mcm // self.denominator()
            count2 = mcm // frac2.denominator()
            self.denominator(self.denominator() * count1, not_min=False)
            frac2.denominator(frac2.denominator() * count2, not_min=False)
            self.numerator(self.numerator() * count1, not_min=False)
            frac2.numerator(frac2.numerator() * count2, not_min=False)
            if self._oper == frac2._oper == '+':
                self.numerator(self.numerator() - frac2.numerator())
            elif self._oper == frac2._oper == '-':
                self.numerator(self.numerator() - frac2.numerator())
            elif self._oper == '-':
                self.numerator(self.numerator() + frac2.numerator())
            else:
                self.numerator(self.numerator() + (frac2.numerator()))
            return self

    def __iadd__(self, others):
        if type(others) in [int, str]:
            frac2 = Fraction(int(others), 1)
        else:
            if others._oper == '+':
                frac2 = Fraction(others.numerator(), others.denominator())
            else:
                frac2 = Fraction(-(others.numerator()), others.denominator())
        if frac2.numerator() == 0:
            return self
        elif self.numerator() == 0:
            self = frac2
            return self
        else:
            mcm = min_common_multiply(self.denominator(), frac2.denominator())
            count1 = mcm // self.denominator()
            count2 = mcm // frac2.denominator()
            self.denominator(self.denominator() * count1, not_min=False)
            frac2.denominator(frac2.denominator() * count2, not_min=False)
            self.numerator(self.numerator() * count1, not_min=False)
            frac2.numerator(frac2.numerator() * count2, not_min=False)
            if self._oper == frac2._oper == '+':
                self.numerator(self.numerator() + frac2.numerator())
            elif self._oper == frac2._oper == '-':
                self.numerator((self.numerator()) + (frac2.numerator()))
            elif self._oper == '-':
                self.numerator((self.numerator()) - frac2.numerator())
            else:
                self.numerator(self.numerator() - (frac2.numerator()))
            return self

    def __mul__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == 0 or self.numerator() == 0:
            return Fraction(0, 0)
        elif (self._oper == other._oper == '+') or (self._oper == other._oper == '-'):
            return Fraction(self.numerator() * other.numerator(), self.denominator() * other.denominator())
        else:
            return Fraction(-(self.numerator() * other.numerator()), self.denominator() * other.denominator())

    def __truediv__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if (self._oper == other._oper == '+') or (self._oper == other._oper == '-'):
            return Fraction(self.numerator() * other.denominator(), self.denominator() * other.numerator())
        else:
            return Fraction(-(self.numerator() * other.denominator()), self.denominator() * other.numerator())

    def __imul__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == 0 or self.numerator() == 0:
            self = Fraction(0, 0)
            return self
        elif (self._oper == other._oper == '+') or (self._oper == other._oper == '-'):
            self._oper = '+'
        else:
            self._oper = '-'
        self.numerator(self.numerator() * other.numerator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __itruediv__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if (self._oper == other._oper == '+') or (self._oper == other._oper == '-'):
            self._oper = '+'
        else:
            self._oper = '-'
        self.numerator(self.numerator() * other.denominator())
        self.denominator(self.denominator() * other.numerator())
        return self

    def reverse(self):
        if self._oper == '+':
            return Fraction(self.denominator(), self.numerator())
        else:
            return Fraction(-self.denominator(), self.numerator())

    def __lt__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == self.numerator() == 0:
            return False
        elif other.numerator() == 0:
            if self._oper == '+':
                return False
            else:
                return True
        elif self.numerator() == 0:
            if other._oper == '+':
                return True
            else:
                return False
        mcm = min_common_multiply(self.denominator(), other.denominator())
        count1 = mcm // self.denominator()
        count2 = mcm // other.denominator()
        self.denominator(self.denominator() * count1, not_min=False)
        other.denominator(other.denominator() * count2, not_min=False)
        self.numerator(self.numerator() * count1, not_min=False)
        other.numerator(other.numerator() * count2, not_min=False)
        if self._oper == other._oper == '+':
            return self.numerator() < other.numerator()
        elif self._oper == other._oper == '-':
            return self.numerator() > other.numerator()
        elif self._oper == '-':
            return True
        else:
            return False

    def __le__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == self.numerator() == 0:
            return True
        elif other.numerator() == 0:
            if self._oper == '+':
                return False
            else:
                return True
        elif self.numerator() == 0:
            if other._oper == '+':
                return True
            else:
                return False
        mcm = min_common_multiply(self.denominator(), other.denominator())
        count1 = mcm // self.denominator()
        count2 = mcm // other.denominator()
        self.denominator(self.denominator() * count1, not_min=False)
        other.denominator(other.denominator() * count2, not_min=False)
        self.numerator(self.numerator() * count1, not_min=False)
        other.numerator(other.numerator() * count2, not_min=False)
        if self._oper == other._oper == '+':
            return self.numerator() <= other.numerator()
        elif self._oper == other._oper == '-':
            return self.numerator() >= other.numerator()
        elif self._oper == '-':
            return True
        else:
            return False

    def __eq__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == self.numerator() == 0:
            return True
        elif other.numerator() == 0 or self.numerator() == 0:
            return False
        mcm = min_common_multiply(self.denominator(), other.denominator())
        count1 = mcm // self.denominator()
        count2 = mcm // other.denominator()
        self.denominator(self.denominator() * count1, not_min=False)
        other.denominator(other.denominator() * count2, not_min=False)
        self.numerator(self.numerator() * count1, not_min=False)
        other.numerator(other.numerator() * count2, not_min=False)
        if self._oper == other._oper and self.numerator() == other.numerator():
            return True
        else:
            return False

    def __ne__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == self.numerator() == 0:
            return False
        elif other.numerator() == 0 or self.numerator() == 0:
            return True
        mcm = min_common_multiply(self.denominator(), other.denominator())
        count1 = mcm // self.denominator()
        count2 = mcm // other.denominator()
        self.denominator(self.denominator() * count1, not_min=False)
        other.denominator(other.denominator() * count2, not_min=False)
        self.numerator(self.numerator() * count1, not_min=False)
        other.numerator(other.numerator() * count2, not_min=False)
        if self._oper == other._oper and self.numerator() == other.numerator():
            return False
        else:
            return True

    def __gt__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == self.numerator() == 0:
            return False
        elif other.numerator() == 0:
            if self._oper == '+':
                return True
            else:
                return False
        elif self.numerator() == 0:
            if other._oper == '+':
                return False
            else:
                return True
        mcm = min_common_multiply(self.denominator(), other.denominator())
        count1 = mcm // self.denominator()
        count2 = mcm // other.denominator()
        self.denominator(self.denominator() * count1, not_min=False)
        other.denominator(other.denominator() * count2, not_min=False)
        self.numerator(self.numerator() * count1, not_min=False)
        other.numerator(other.numerator() * count2, not_min=False)
        if self._oper == other._oper == '+':
            return self.numerator() > other.numerator()
        elif self._oper == other._oper == '-':
            return self.numerator() < other.numerator()
        elif self._oper == '-':
            return False
        else:
            return True

    def __ge__(self, other):
        if type(other) in [int, str]:
            other = Fraction(int(other), 1)
        if other.numerator() == self.numerator() == 0:
            return True
        elif other.numerator() == 0:
            if self._oper == '+':
                return True
            else:
                return False
        elif self.numerator() == 0:
            if other._oper == '+':
                return False
            else:
                return True
        mcm = min_common_multiply(self.denominator(), other.denominator())
        count1 = mcm // self.denominator()
        count2 = mcm // other.denominator()
        self.denominator(self.denominator() * count1, not_min=False)
        other.denominator(other.denominator() * count2, not_min=False)
        self.numerator(self.numerator() * count1, not_min=False)
        other.numerator(other.numerator() * count2, not_min=False)
        if self._oper == other._oper == '+':
            return self.numerator() >= other.numerator()
        elif self._oper == other._oper == '-':
            return self.numerator() <= other.numerator()
        elif self._oper == '-':
            return False
        else:
            return True


a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)

# 1/1 2/1 1/3 1/1
# False False
# True True False True
