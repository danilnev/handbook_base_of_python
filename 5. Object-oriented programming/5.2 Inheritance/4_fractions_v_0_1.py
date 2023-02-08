def max_common_divisor(num1, num2):
    while num1 % num2 != 0 and num2 % num1 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return min([num1, num2])


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            num1, num2 = map(int, list(args[0].split('/')))
        else:
            num1, num2 = args
        mcd = max_common_divisor(num1, num2)
        num1 //= mcd
        num2 //= mcd
        self.numer = num1
        self.denomin = num2

    def numerator(self, *args):
        if len(args) == 0:
            return self.numer
        else:
            self.numer = args[0]
            mcd = max_common_divisor(self.numer, self.denomin)
            self.numer //= mcd
            self.denomin //= mcd

    def denominator(self, *args):
        if len(args) == 0:
            return self.denomin
        else:
            self.denomin = args[0]
            if max_common_divisor(self.numer, self.denomin) != min(self.numer, self.denomin):
                self.numer //= max_common_divisor(self.numer, self.denomin)
                self.denomin //= max_common_divisor(self.numer, self.denomin)

    def __str__(self):
        return f'{self.numer}/{self.denomin}'

    def __repr__(self):
        return f'Fraction({self.numer}, {self.denomin})'


frac = Fraction(3, 210)
print(frac, repr(frac))
frac.numerator(10)
print(frac.numerator(), frac.denominator())
frac.denominator(2)
print(frac.numerator(), frac.denominator())
