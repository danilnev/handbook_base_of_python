def max_common_divisor(num1, num2):
    while num1 % num2 != 0 and num2 % num1 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return min([num1, num2])


def min_common_multiply(num1, num2):
    i = max(num1, num2)
    while True:
        if i % num1 == 0 and i % num2 == 0:
            return i
        i += 1


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            num1, num2 = map(int, list(args[0].split('/')))
        else:
            num1, num2 = args
        if num1 < 0 and num2 < 0:
            _oper = '+'
            num1 = -num1
            num2 = -num2
        elif num1 >= 0 and num2 >= 0:
            _oper = '+'
        elif num1 < 0:
            _oper = '-'
            num1 = -num1
        else:
            _oper = '-'
            num2 = -num2
        mcd = max_common_divisor(num1, num2)
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
        if others._oper == '+':
            frac2 = Fraction(others.numerator(), others.denominator())
        else:
            frac2 = Fraction(-(others.numerator()), others.denominator())
        mcm = min_common_multiply(frac1.denominator(), frac2.denominator())
        count1 = mcm // frac1.denominator()
        count2 = mcm // frac2.denominator()
        frac1.denominator(frac1.denominator() * count1, not_min=False)
        frac2.denominator(frac2.denominator() * count2, not_min=False)
        frac1.numerator(frac1.numerator() * count1, not_min=False)
        frac2.numerator(frac2.numerator() * count2, not_min=False)
        if frac1._oper == frac2._oper == '+':
            frac3 = Fraction(frac1.numerator() + frac2.numerator(), frac1.denominator())
        elif frac1._oper == frac2._oper == '-':
            frac3 = Fraction(-(frac1.numerator()) + -(frac2.numerator()), frac1.denominator())
        elif frac1._oper == '-':
            frac3 = Fraction(-(frac1.numerator()) + frac2.numerator(), frac1.denominator())
        else:
            frac3 = Fraction(frac1.numerator() + -(frac2.numerator()), frac1.denominator())
        return frac3

    def __sub__(self, others):
        if self._oper == '+':
            frac1 = Fraction(self.numerator(), self.denominator())
        else:
            frac1 = Fraction(-(self.numerator()), self.denominator())
        if others._oper == '+':
            frac2 = Fraction(others.numerator(), others.denominator())
        else:
            frac2 = Fraction(-(others.numerator()), others.denominator())
        mcm = min_common_multiply(frac1.denominator(), frac2.denominator())
        count1 = mcm // frac1.denominator()
        count2 = mcm // frac2.denominator()
        frac1.denominator(frac1.denominator() * count1, not_min=False)
        frac2.denominator(frac2.denominator() * count2, not_min=False)
        frac1.numerator(frac1.numerator() * count1, not_min=False)
        frac2.numerator(frac2.numerator() * count2, not_min=False)
        if frac1._oper == frac2._oper == '+':
            frac3 = Fraction(frac1.numerator() - frac2.numerator(), frac1.denominator())
        elif frac1._oper == frac2._oper == '-':
            frac3 = Fraction(-(frac1.numerator()) - -(frac2.numerator()), frac1.denominator())
        elif frac1._oper == '-':
            frac3 = Fraction(-frac1.numerator() - frac2.numerator(), frac1.denominator())
        else:
            frac3 = Fraction(frac1.numerator() - -(frac2.numerator()), frac1.denominator())
        return frac3

    def __isub__(self, others):
        if type(others) == int:
            frac2 = Fraction(others, abs(others))
        else:
            if others._oper == '+':
                frac2 = Fraction(others.numerator(), others.denominator())
            else:
                frac2 = Fraction(-(others.numerator()), others.denominator())
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
        if type(others) == int:
            frac2 = Fraction(others, abs(others))
        else:
            if others._oper == '+':
                frac2 = Fraction(others.numerator(), others.denominator())
            else:
                frac2 = Fraction(-(others.numerator()), others.denominator())
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


# print(Fraction(-1, 3) + Fraction(2, 9))
