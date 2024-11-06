from core import generic_module as gm
# частное от деления многочленов
from core.DIV_PP_P import DIV_PP_P
# умножение многочленов
from core.MUL_PP_P import MUL_PP_P
# разность многочленов
from core.SUB_PP_P import SUB_PP_P
from data_types import *
import copy

class MOD_PP_P(gm.AbstractModule):
    # добавляем функции, которыми пользуемся
    def __init__(self):
        self.div = DIV_PP_P()
        self.mul = MUL_PP_P()
        self.sub = SUB_PP_P()

    def execute(self, args):
        # проверка поданных аргументов
        if len(args) != 2:
            raise ValueError("Function MOD_PP_P takes only 2 args.")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type in MOD_PP_P: must be Polynomial.")


        # находим частное, умножаем на делитель и отнимаем полученный полином от делимого
        div_pol = self.div.execute([copy.deepcopy(args[0]), copy.deepcopy(args[1])])[0]
        mul_for_sub_pol = self.mul.execute([args[1], div_pol])[0]
        result_polynomial = self.sub.execute([args[0], mul_for_sub_pol])[0]
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        pass
