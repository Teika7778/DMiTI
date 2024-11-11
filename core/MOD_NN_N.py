from core.DIV_NN_N import DIV_NN_N
from core.SUB_NN_N import SUB_NN_N
from core.MUL_NN_N import MUL_NN_N
from core import generic_module as gm
from data_types import *
import copy

class MOD_NN_N(gm.AbstractModule):
    def execute(self, args):
        # делаю ноль проверок, т.к. все они реализованы в неполном частном
        quotient = DIV_NN_N().execute(args)[0]  # частное
        divisible = Natural(copy.deepcopy(args[0].numbers))  # делимое
        divider = Natural(copy.deepcopy(args[1].numbers)) # делитель
        multiplied = MUL_NN_N().execute([quotient, divider])[0] # частное на делитель
        return SUB_NN_N().execute([divisible, multiplied]) # считаем остаток как разность

    def reference(self) -> str:
        return (
            "The remainder from dividing the first natural number by the second natural number [NATURAL, NATURAL -> NATURAL]\n"
            "Arguments:\n"
            "\t1: Natural - divisible\n"
            "\t2: Natural - divider\n"
            "Returns:\n"
            "\t1: Natural - remainder\n"
            "Author: Alexey Maidurov\n")
