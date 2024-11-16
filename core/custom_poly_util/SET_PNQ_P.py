from core import generic_module as gm
from data_types import *
import copy


class SET_PNQ_P(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 3:
            raise ValueError("Improper arguments: function takes only 2 arg")
        poly = copy.deepcopy(args[0])
        nat = args[1]
        num = copy.deepcopy(args[2])
        if not isinstance(poly, Polynomial) or not isinstance(nat, Natural) or not isinstance(num, Rational):
            raise ValueError("Invalid data type")
        nat_i = int(''.join(list(map(str, nat.numbers)))[::-1])
        if num.numerator.natural == [0] and nat_i >= len(poly.coefficients):
            return [poly]
        while nat_i >= len(poly.coefficients):
            poly.coefficients = poly.coefficients + [Rational(Integer(Natural([0])),
                                                              Natural([1]))]
        poly.coefficients[nat_i] = num
        poly.simplify()
        return [poly]

    def reference(self) -> str:
        return ("Set coefficent of polynomial [POLYNOMIAL, NATURAL, RATIONAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - polynomial\n"
                "\t2: Natural - coefficient number\n"
                "\t2: Rational - new value\n"
                "Returns:\n"
                "\t1: Polynomial - result\n"
                "Author: Evdokimov Maxim \n")
