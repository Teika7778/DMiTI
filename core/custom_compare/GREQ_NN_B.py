from core import generic_module as gm
from data_types import *
from core.custom_compare.GRE_NN_B import GRE_NN_B
from core.custom_compare.EQ_NN_B import EQ_NN_B

class GREQ_NN_B(gm.AbstractModule):
    def __init__(self):
        self.cmp = GRE_NN_B()
        self.eq = EQ_NN_B()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, Natural) or not isinstance(arg2, Natural):  # проверка типа
            raise ValueError("Invalid data type: args must be natural")
        cmp_1 = self.cmp.execute([arg1, arg2])[0]
        cmp_2 = self.eq.execute([arg2, arg1])[0]
        return [cmp_1 or cmp_2]

    def reference(self) -> str:
        return ("Natural number comparator [NATURAL, NATURAL -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Natural - first term\n"
                "\t2: Natural - second term\n"
                "Returns:\n"
                "\t1: Boolean - result, TRUE only if terms are equal or if first is greater\n"
                "Author: Evdokimov Maxim \n")