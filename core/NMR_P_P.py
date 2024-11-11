import copy
from core import generic_module as gm
# НОД многочленов
from core.GCF_PP_P import GCF_PP_P
# производная многочлена
from core.DER_P_P import DER_P_P
# частное от деления
from core.DIV_PP_P import DIV_PP_P
from data_types import *

class NMR_P_P(gm.AbstractModule):
    # добавляем функции, которыми пользуемся
    def __init__(self):
        self.gcf = GCF_PP_P()
        self.der = DER_P_P()
        self.div = DIV_PP_P()

    def execute(self, args):
        # проверка поданных аргументов
        if len(args) != 1:
            raise ValueError("Function NMR_P_P takes only 1 arg.")
        if not (isinstance(args[0], Polynomial)):
            raise ValueError("Invalid data type in NMR_P_P: must be Polynomial.")

        pol = copy.deepcopy(args[0])
        # находим производную
        der_pol = self.der.execute([pol])[0]
        # НОД многочлена и производной
        gcf_pol_der_pol = self.gcf.execute([pol, der_pol])[0]
        # делим и получаем нужный многочлен
        result_polynomial = self.div.execute([pol, gcf_pol_der_pol])[0]
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        return ("Transformation of polynomial - multiple roots to simple roots [POLYNOMIAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - to transform\n"
                "Returns:\n"
                "\t1: Polynomial - transformed result\n"
                "Author: Anastasia Dorogushina\n")
