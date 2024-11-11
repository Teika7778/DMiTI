from core import generic_module as gm
from data_types import *
from core.MOD_PP_P import MOD_PP_P
from core.RED_Q_Q import RED_Q_Q
from core.DEG_P_N import DEG_P_N
from core.COM_NN_D import COM_NN_D
from core.NZER_N_B import NZER_N_B

import copy


class GCF_PP_P(gm.AbstractModule):
    def __init__(self):
        self.mod_pp = MOD_PP_P()
        self.red = RED_Q_Q()
        self.deg = DEG_P_N()
        self.comp = COM_NN_D()
        self.nzer = NZER_N_B()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type:  must be polynomial")
        result_a = copy.deepcopy(args[0])  # Копии многочленов
        result_b = copy.deepcopy(args[1])

        if self.deg.execute([result_a])[0].numbers[0] == 0:
            return [Polynomial([Rational(Integer(Natural([1]), True), Natural([1]))])]
        if self.deg.execute([result_b])[0].numbers[0] == 0:
            return [Polynomial([Rational(Integer(Natural([1]), True), Natural([1]))])]

        # Алгоритм Евклида делением
        # Пока степени обоих не равны нулю

        while self.comp.execute([self.deg.execute([result_b])[0], Natural([1])])[0].numbers[0] != 1 and self.comp.execute([self.deg.execute([result_b])[0], self.deg.execute([result_a])[0]])[0].numbers[0] == 1:  # пока result_b < result_a
            result_a, result_b = result_b, self.mod_pp.execute([result_a, result_b])[0]  # Меняем значение местами, заменяя b делением с остатком a на b
        return [result_a]

    def reference(self) -> str:
        return ("Greatest common divisor of polynomials [POLYNOMIAL. POLYNOMIAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - first\n"
                "\t2: Polynomial - second\n"
                "Returns:\n"
                "\t1: Polynomial - greatest common divisor\n"
                "Author: Gleb Khorchev\n")
