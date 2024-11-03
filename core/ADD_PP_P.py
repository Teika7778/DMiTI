from core import generic_module as gm
# сложение дробей
from core.ADD_QQ_Q import ADD_QQ_Q
from data_types import *
import copy

class ADD_PP_P(gm.AbstractModule):
    # добавляем функции, которыми пользуемся
    def __init__(self):
        self.add = ADD_QQ_Q()

    def execute(self, args):
        pol1, pol2 = args
        # максимальная длина многочленов
        k = max(len(pol1.coefficients), len(pol2.coefficients))
        result_coefficients = []
        # в цикле делаем сложение коэффициентов
        for i in range(k):
            coef1 = pol1.coefficients[k] if len(pol1.coefficients) > k else Rational(Integer(Natural([0]), True), Natural([1]))
            coef2 = pol2.coefficients[k] if len(pol2.coefficients) > k else Rational(Integer(Natural([0]), True), Natural([1]))
            result_coefficients.append(self.add.execute([coef1, coef2])[0])

        # делаем результат и возвращаем полиномом
        result_polynomial = Polynomial(result_coefficients)
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        pass