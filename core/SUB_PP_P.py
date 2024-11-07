from core import generic_module as gm
from core.SUB_QQ_Q import SUB_QQ_Q
import copy
from data_types import *

class SUB_PP_P(gm.AbstractModule):
    # добавляем функцию, которой пользуемся
    def __init__(self):
        self.sub_q = SUB_QQ_Q()

    def execute(self, args):
        # проверка поданных аргументов
        if len(args) != 2:
            raise ValueError("Function SUB_PP_P takes only 2 args.")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type in SUB_PP_P: must be Polynomial.")
        
        # сравниваем длины полиномов, чтобы взять большую для вычитания
        p1 = copy.deepcopy(args[0])
        p2 = copy.deepcopy(args[1])
        max_len = max(len(p1.coefficients), len(p2.coefficients))
        result_coefficients = []

        for i in range(max_len):
            # подтягиваем равное количество коэффициентов
            coef1 = p1.coefficients[i] if i < len(p1.coefficients) else Rational(Integer(Natural([0]), True), Natural([1]))
            coef2 = p2.coefficients[i] if i < len(p2.coefficients) else Rational(Integer(Natural([0]), True), Natural([1]))

            # вычитание коэффициентов
            result_coef = self.sub_q.execute([coef1, coef2])[0]
            result_coefficients.append(result_coef)

        # делаем результат и возвращаем полиномом
        result_polynomial = Polynomial(result_coefficients)
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        return ("Subtracting a polynomial from a polynomial [POLYNOMIAL, POLYNOMIAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - minuend number\n"
                "\t2: Polynomial - subtrahend number\n"
                "Returns:\n"
                "\t1: Polynomial - difference\n"
                "Author: Anastasia Dorogushina\n")
