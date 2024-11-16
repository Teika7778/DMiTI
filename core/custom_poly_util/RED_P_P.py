from core import generic_module as gm
from data_types import *
from core.RED_Q_Q import RED_Q_Q
import copy


class RED_P_P(gm.AbstractModule):
    def __init__(self):
        self.mod = RED_Q_Q()

    def execute(self, args):
        if not len(args) == 1:
            raise ValueError("Improper arguments: function takes only 2 arg")
        poly = copy.deepcopy(args[0])
        if not isinstance(poly, Polynomial):  # проверка типа
            raise ValueError("Invalid data type")
        for i in range(len(poly.coefficients)):
            poly.coefficients[i] = self.mod.execute([poly.coefficients[i]])[0]
        return [poly]

    def reference(self) -> str:
        return ("Reduce all coefficients of given polynomial [POLYNOMIAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - polynomial\n"
                "Returns:\n"
                "\t1: Polynomial - reduced polynomial\n"
                "Author: Evdokimov Maxim \n")
