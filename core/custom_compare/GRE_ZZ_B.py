from core import generic_module as gm
from data_types import *
from core.SUB_ZZ_Z import SUB_ZZ_Z


class GRE_ZZ_B(gm.AbstractModule):
    def __init__(self):
        self.sub = SUB_ZZ_Z()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, Integer) or not isinstance(arg2, Integer):  # проверка типа
            raise ValueError("Invalid data type: args must be integer")
        res = self.sub.execute([arg1, arg2])[0]
        return [res.is_positive and not res.natural.numbers == [0]]

    def reference(self) -> str:
        return ("Integer comparator [INTEGER, INTEGER -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Integer - first term\n"
                "\t2: Integer - second term\n"
                "Returns:\n"
                "\t1: Boolean - result, TRUE only if first term is greater then second\n"
                "Author: Evdokimov Maxim \n")