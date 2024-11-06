from data_types import *


# натуральное число это набор цифр, где первое это не 0
# целое число это знак (+-) и натуральное число
# рациональное число это пара натуральное-натуральное, разделенная знаком / и имеющая знак
# полнином это последовательность рациональных чисел, разделенных знаком ,. ПОНИНОМ МОЖЕТ НАЧИНАТЬСЯ с приписки P
class DataTypeParser:
    def __init__(self):
        self.valid = list(map(str, range(10)))

    def str_to_datatype(self, string: str):
        if len(string) == 0:
            raise ValueError()
        if string[0] == 'P':
            string = string[1:]
            return self.parse_polynomial(string)
        if ',' in string:
            return self.parse_polynomial(string)
        if '/' in string:
            return self.parse_rational(string)
        if '+' in string or '-' in string:
            return self.parse_integer(string)
        return self.parse_natural(string)

    def parse_natural(self, string: str):
        for char in string:
            if char not in self.valid:
                raise ValueError()
        if len(string) == 0:
            raise ValueError()
        if string[0] == '0':
            raise ValueError()
        nums = list(map(int, list(string)[::-1]))
        return Natural(nums)

    def parse_integer(self, string: str):
        if len(string) == 0:
            raise ValueError()
        if string[0] == '+':
            return Integer(self.parse_natural(string[1:]))
        if string[0] == '-':
            return Integer(self.parse_natural(string[1:]), is_positive=False)

    def parse_rational(self, string: str):
        if len(string) == 0:
            raise ValueError()
        if '/' not in string:
            top = self.parse_integer(string)
            bot = Natural([1])
        else:
            sliced = string.split('/')
            if len(sliced) != 2:
                raise ValueError()
            if sliced[1] == '0':
                raise ValueError()
            top = self.parse_integer(sliced[0])
            bot = self.parse_natural(sliced[1])
        return Rational(top, bot)

    def parse_polynomial(self, string: str):
        coefficients = string.split(',')
        coefficients_t = []
        for coefficient in coefficients:
            coefficient_t = self.parse_rational(coefficient)
            coefficients_t.append(coefficient_t)
        return Polynomial(coefficients_t)
