from core import generic_module as gm
from data_types import *
from core.COM_NN_D import COM_NN_D


class GRE_NN_B(gm.AbstractModule):
    def __init__(self):
        self.cmp = COM_NN_D()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, Natural) or not isinstance(arg2, Natural):  # проверка типа
            raise ValueError("Invalid data type: args must be natural")
        digit = self.cmp.execute([arg1, arg2])[0].numbers[0]
        return [digit == 2]

    def reference(self) -> str:
        return ("Natural number comparator [NATURAL, NATURAL -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Natural - first term\n"
                "\t2: Natural - second term\n"
                "Returns:\n"
                "\t1: Boolean - result, TRUE only if first term is greater then second\n"
                "Author: Evdokimov Maxim \n")
