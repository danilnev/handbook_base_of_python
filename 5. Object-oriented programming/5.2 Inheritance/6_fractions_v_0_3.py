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
            oper = '+'
            num1 = -num1
            num2 = -num2
        elif num1 >= 0 and num2 >= 0:
            oper = '+'
        elif num1 < 0:
            oper = '-'
            num1 = -num1
        else:
            oper = '-'
            num2 = -num2
        mcd = max_common_divisor(num1, num2)
        num1 //= mcd
        num2 //= mcd
        self.numer = num1
        self.denomin = num2
        self.oper = oper

    def numerator(self, *args):
        if len(args) == 0:
            return self.numer
        else:
            number = args[0]
            if number < 0:
                number = -number
                if self.oper == '+':
                    self.oper = '-'
                else:
                    self.oper = '+'
            self.numer = number
            mcd = max_common_divisor(self.numer, self.denomin)
            self.numer //= mcd
            self.denomin //= mcd

    def denominator(self, *args):
        if len(args) == 0:
            return self.denomin
        else:
            number = args[0]
            if number < 0:
                number = -number
                if self.oper == '+':
                    self.oper = '-'
                else:
                    self.oper = '+'
            self.denomin = number
            mcd = max_common_divisor(self.numer, self.denomin)
            self.numer //= mcd
            self.denomin //= mcd

    def __str__(self):
        if self.oper == '+':
            return f'{self.numer}/{self.denomin}'
        else:
            return f'-{self.numer}/{self.denomin}'

    def __repr__(self):
        if self.oper == '+':
            return f'Fraction(\'{self.numer}/{self.denomin}\')'
        else:
            return f'Fraction(\'-{self.numer}/{self.denomin}\')'

    def __neg__(self):
        if self.oper == '+':
            return Fraction(-self.numer, self.denomin)
        else:
            return Fraction(self.numer, self.denomin)

    def __add__(self, others):
        if self.oper == '+':
            frac1 = Fraction(self.numerator(), self.denominator())
        else:
            frac1 = Fraction(-(self.numerator()), self.denominator())
        if others.oper == '+':
            frac2 = Fraction(others.numerator(), others.denominator())
        else:
            frac2 = Fraction(-(others.numerator()), others.denominator())
        mcm = min_common_multiply(frac1.denomin, frac2.denomin)
        count1 = mcm // frac1.denomin
        count2 = mcm // frac2.denomin
        frac1.denominator(frac1.denomin * (count1))
        frac2.denominator(frac2.denomin * (count2))
        frac1.numerator(frac1.numer * count1)
        frac2.numerator(frac2.numer * count2)
        if frac1.oper == frac2.oper == '+':
            frac3 = Fraction(frac1.numerator() + frac2.numerator(), frac1.denominator())
        elif frac1.oper == frac2.oper == '-':
            frac3 = Fraction(-(frac1.numerator()) + -(frac2.numerator()), frac1.denominator())
        elif frac1.oper == '-':
            frac3 = Fraction(-(frac1.numerator()) + frac2.numerator(), frac1.denominator())
        else:
            frac3 = Fraction(frac1.numerator() + -(frac2.numerator()), frac1.denominator())
        return frac3

    def __sub__(self, others):
        if self.oper == '+':
            frac1 = Fraction(self.numerator(), self.denominator())
        else:
            frac1 = Fraction(-(self.numerator()), self.denominator())
        if others.oper == '+':
            frac2 = Fraction(others.numerator(), others.denominator())
        else:
            frac2 = Fraction(-(others.numerator()), others.denominator())
        mcm = min_common_multiply(frac1.denomin, frac2.denomin)
        count1 = mcm // frac1.denomin
        count2 = mcm // frac2.denomin
        frac1.denominator(frac1.denomin * (count1))
        frac2.denominator(frac2.denomin * (count2))
        frac1.numerator(frac1.numer * count1)
        frac2.numerator(frac2.numer * count2)
        if frac1.oper == frac2.oper == '+':
            frac3 = Fraction(frac1.numerator() - frac2.numerator(), frac1.denominator())
        elif frac1.oper == frac2.oper == '-':
            frac3 = Fraction(-(frac1.numerator()) - -(frac2.numerator()), frac1.denominator())
        elif frac1.oper == '-':
            frac3 = Fraction(-(frac1.numerator()) - frac2.numerator(), frac1.denominator())
        else:
            frac3 = Fraction(frac1.numerator() - -(frac2.numerator()), frac1.denominator())
        return frac3



a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)
