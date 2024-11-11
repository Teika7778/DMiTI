from core import generic_module as gm
from data_types import *
import copy


class INT_Q_B(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 1: #проверка на получение единственного аргумента
            raise ValueError("Improper arguments: function takes only 1 arg")
        rational = copy.deepcopy(args[0])
        if not isinstance(rational, Rational):  # проверка типа
            raise ValueError("Invalid data type: must be rational")
        natural = Natural([1])
        if rational.denominator.numbers == natural.numbers:
            return [True]
        else:
            return [False]
    
    def reference(self) -> str:
        return ("Checking a reduced fractional by an integer [RATIONAL -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Rational - reduced fractional\n"
                "Returns:\n"
                "\t1: Boolean - result (true - is not zero, false - is zero)\n"
                "Author: Timofey Komarenko\n")
