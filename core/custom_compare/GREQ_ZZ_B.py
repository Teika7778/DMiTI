from core import generic_module as gm
from data_types import *
from core.custom_compare.GRE_ZZ_B import GRE_ZZ_B
from core.custom_compare.EQ_ZZ_B import EQ_ZZ_B

class GREQ_ZZ_B(gm.AbstractModule):
    def __init__(self):
        self.cmp = GRE_ZZ_B()
        self.eq = EQ_ZZ_B()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, Integer) or not isinstance(arg2, Integer):  # проверка типа
            raise ValueError("Invalid data type: args must be integer")
        cmp_1 = self.cmp.execute([arg1, arg2])[0]
        cmp_2 = self.eq.execute([arg2, arg1])[0]
        return [cmp_1 or cmp_2]

    def reference(self) -> str:
        return ("Natural number comparator [INTEGER, INTEGER -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Integer - first term\n"
                "\t2: Integer - second term\n"
                "Returns:\n"
                "\t1: Boolean - result, TRUE only if terms are equal or if first is greater\n"
                "Author: Evdokimov Maxim \n")