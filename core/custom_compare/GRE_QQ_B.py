from core import generic_module as gm
from data_types import *
from core.SUB_QQ_Q import SUB_QQ_Q


class GRE_QQ_B(gm.AbstractModule):
    def __init__(self):
        self.sub = SUB_QQ_Q()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, Rational) or not isinstance(arg2, Rational):  # проверка типа
            raise ValueError("Invalid data type: args must be rational")
        res = self.sub.execute([arg1, arg2])[0]
        return [res.numerator.is_positive and not res.numerator.natural.numbers == [0]]

    def reference(self) -> str:
        return ("Rational comparator [RATIONAL, RATIONAL -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Rational - first term\n"
                "\t2: Rational - second term\n"
                "Returns:\n"
                "\t1: Boolean - result, TRUE only if first term is greater then second\n"
                "Author: Evdokimov Maxim \n")