from core import generic_module as gm
# частное от деления многочленов
from core.DIV_PP_P import DIV_PP_P
# умножение многочленов
from core.MUL_PP_P import MUL_PP_P
# разность многочленов
from core.SUB_PP_P import SUB_PP_P
from data_types import *

class MOD_PP_P(gm.AbstractModule):
    # добавляем функции, которыми пользуемся
    def __init__(self):
        self.div = DIV_PP_P()
        self.mul = MUL_PP_P()
        self.sub = SUB_PP_P()

    def execute(self, args):
        # находим частное, умножаем на делитель и отнимаем полученный полином от делимого
        div_pol = self.div.execute(args)
        mul_for_sub_pol = self.mul.execute([args[1], div_pol])
        result_polynomial = self.sub.execute([args[0], mul_for_sub_pol])
        result_polynomial.simplify()

        return result_polynomial
