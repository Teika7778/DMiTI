from core import generic_module as gm
from data_types import *
import copy


class GET_PN_Q(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        poly = args[0]
        nat = args[1]
        if not isinstance(poly, Polynomial) or not isinstance(nat, Natural):  # проверка типа
            raise ValueError("Invalid data type")
        nat_i = int(''.join(list(map(str, nat.numbers)))[::-1])
        if nat_i >= len(poly.coefficients):
            return [Rational(Integer(Natural([0])),
                             Natural([1]))]
        else:
            return [copy.deepcopy(poly.coefficients[nat_i])]

    def reference(self) -> str:
        return ("Get coefficent of polynomial [POLYNOMIAL, NATURAL -> RATIONAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - polynomial\n"
                "\t2: Natural - coefficient number\n"
                "Returns:\n"
                "\t1: Rational - said coefficient or 0, if no such\n"
                "Author: Evdokimov Maxim \n")