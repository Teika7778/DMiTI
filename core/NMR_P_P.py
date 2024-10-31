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
        pol = args[0]
        # находим производную
        der_pol = self.der.execute(args)
        # НОД многочлена и производной
        gcf_pol_der_pol = self.gcf.execute([pol, der_pol])
        # делим и получаем нужный многочлен
        result_polynomial = self.div.execute([pol, gcf_pol_der_pol])
        result_polynomial.simplify()

        return result_polynomial
