from core import generic_module as gm
from core.MUL_QQ_Q import MUL_QQ_Q
from data_types import *

class DER_P_P(gm.AbstractModule):
    # добавляем функцию, которой пользуемся
    def __init__(self):
        self.module = MUL_QQ_Q()

    def execute(self, args):
        # проверка поданных аргументов
        if len(args) != 1:
            raise ValueError("Function DER_P_P takes only 1 arg.")
        if not (isinstance(args[0], Polynomial)):
            raise ValueError("Invalid data type in DER_P_P: must be Polynomial.")
        # берём полином и также создаём массив коэффициентов
        p = args[0]
        result_coefficients = []
        if len(p.coefficients) == 1:
            result_coefficients.append(Rational(Integer(Natural([0]), True), Natural([1])))
        # считаем производную, пропуская первый член при x^0
        for i in range(1, len(p.coefficients), 1):
            # стряпаем рациональное число из соответствующей степени
            q_i = Rational(Integer(Natural([i]), True), Natural([1]))
            # умножаем степень на коэффициент и по сути сдвигаем на степень ниже из-за пропуска
            result_coefficients.append(self.module.execute([q_i, p.coefficients[i]])[0])

        # делаем результат и возвращаем полиномом
        result_polynomial = Polynomial(result_coefficients)
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        pass
