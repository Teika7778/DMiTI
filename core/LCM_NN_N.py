from core import generic_module as gm
from data_types import *
from core.GCF_NN_N import GCF_NN_N
from core.MUL_NN_N import MUL_NN_N
from core.DIV_NN_N import DIV_NN_N



class LCM_NN_N(gm.AbstractModule):
    def __init__(self):
        self.gcf_nn = GCF_NN_N()
        self.mul_nn = MUL_NN_N()
        self.div_nn = DIV_NN_N()


    def execute(self, args):
        if len(args) != 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError("Invalid data type: must be natural")

        mul_args = self.mul_nn.execute([args[0], args[1]])[0]  # Произведение переданных натуральных чисел
        gcf_args = self.gcf_nn.execute([args[0], args[1]])[0]  # НОД переданных натуральных чисел
        return self.div_nn.execute([mul_args, gcf_args])  # Подсчет НОК

    def reference(self) -> str:
        return ("Least common multiple of natural numbers [NATURAL. NATURAL -> NATURAL]\n"
                "Arguments:\n"
                "\t1: Natural - first\n"
                "\t2: Natural - second\n"
                "Returns:\n"
                "\t1: Natural - least common multiple\n"
                "Author: Artyom Grebenshchikov\n")
