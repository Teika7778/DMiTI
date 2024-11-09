from core import generic_module as gm
from data_types import *
from core.MOD_PP_P import MOD_PP_P
import copy


class GCF_PP_P(gm.AbstractModule):
    def __init__(self):
        self.mod_pp_p = MOD_PP_P()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type:  must be polynomial")
        arg0_copy = copy.deepcopy(args[0])  # Копии многочленов
        arg1_copy = copy.deepcopy(args[1])
        # Алгоритм Евклида делением
        # Пока степени обоих не равны нулю
        while len(arg0_copy.coefficients) > 1 and len(arg1_copy.coefficients) > 1:
            # если степень первого больше
            if len(arg0_copy.coefficients) > len(arg1_copy.coefficients):
                # делим на второй
                arg0_copy = self.mod_pp_p.execute([arg0_copy, arg1_copy])[0]
            else:  # иначе
                arg1_copy = self.mod_pp_p.execute([arg1_copy, arg0_copy])[0]  # делим на первый

        if len(arg0_copy.coefficients) == 1:  # проверяем, какой не равен нулю
            return [arg1_copy]
        else:
            return [arg0_copy]

    def reference(self) -> str:
        pass
