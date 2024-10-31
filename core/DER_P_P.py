from core import generic_module as gm
from core.MUL_QQ_Q import MUL_QQ_Q
from data_types import *

class DER_P_P(gm.AbstractModule):
    # добавляем функцию, которой пользуемся
    def __init__(self):
        self.module = MUL_QQ_Q()

    def execute(self, args):
        # берём полином и также создаём массив коэффициентов
        p = args[0]
        result_coefficients = []
        # считаем производную, пропуская первый член при x^0
        for i in range(1, len(p.coefficients), 1):
            # стряпаем рациональное число из соответствующей степени
            q_i = Rational(Integer(Natural([i]), True), Natural([1]))
            # умножаем степень на коэффициент и по сути сдвигаем на степень ниже из-за пропуска
            result_coefficients.append(self.module.execute([q_i, p.coefficients[i]]))

        # делаем результат и возвращаем полиномом
        result_polynomial = Polynomial(result_coefficients)
        result_polynomial.simplify()

        return result_polynomial
