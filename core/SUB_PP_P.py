from core import generic_module as gm
from core.SUB_QQ_Q import SUB_QQ_Q
from data_types import *

class SUB_PP_P(gm.AbstractModule):
    # добавляем функцию, которой пользуемся
    def init(self):
        self.sub_q = SUB_QQ_Q()

    def execute(self, args):
        # сравниваем длины полиномов, чтобы взять большую для вычитания
        p1 = args[0]
        p2 = args[1]
        max_len = max(len(p1.coefficients), len(p2.coefficients))
        result_coefficients = []

        for i in range(max_len):
            # подтягиваем равное количество коэффициентов
            coef1 = p1.coefficients[i] if i < len(p1.coefficients) else Rational(Integer(Natural([0])), Natural([1]))
            coef2 = p2.coefficients[i] if i < len(p2.coefficients) else Rational(Integer(Natural([0])), Natural([1]))

            # вычитание коэффициентов
            result_coef = self.sub_q.execute([coef1, coef2])
            result_coefficients.append(result_coef)

        # делаем результат и возвращаем полиномом
        result_polynomial = Polynomial(result_coefficients)
        result_polynomial.simplify()

        return result_polynomial