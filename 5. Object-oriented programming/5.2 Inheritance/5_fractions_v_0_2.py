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


# a = Fraction('-1/2')
# b = -a
# print(a, b, a is b)
# b.numerator(-b.numerator())
# a.denominator(-3)
# print(a, b)
# print(a.numerator(), a.denominator())
# print(b.numerator(), b.denominator())


