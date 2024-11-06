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
        pass

zero_coef_1 = Rational(Integer(Natural([0, 2]), False), Natural([4])) # -5
first_coef_1 = Rational(Integer(Natural([2, 3]), False), Natural([4])) # 8
second_coef_1 = Rational(Integer(Natural([2, 1]), False), Natural([4])) # -3
third_coef_1 = Rational(Integer(Natural([6, 1]), False), Natural([4])) # -4
forth_coef_1 = Rational(Integer(Natural([8]), False), Natural([4])) # 2
first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1, forth_coef_1]) # -5+8x-3x^2-4x^3+2x^4+x^6
zero_coef_2 = Rational(Integer(Natural([2])), Natural([2])) # 1
first_coef_2 = Rational(Integer(Natural([3]), False), Natural([2])) # -1
second_coef_2 = Rational(Integer(Natural([6]), False), Natural([2])) # 1
third_coef_2 = Rational(Integer(Natural([3]), False), Natural([2])) # 0
forth_coef_2 = Rational(Integer(Natural([4]), False), Natural([2])) # 0
second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2, forth_coef_2]) # 1-x+x^2+x^5
A = SUB_PP_P()
result = A.execute([second_polym, first_polym])[0]
print(f'\n\n{second_polym} - \n {first_polym} = \n{result}, {len(result.coefficients)}')
print(str(result.coefficients[-1].numerator))
print(*(str(i) for i in result.coefficients))

coef = Rational(Integer(Natural([0]), False), Natural([52]))
polu = Polynomial(coef)
print()