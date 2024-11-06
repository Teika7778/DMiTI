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
        mul_for_sub_pol = self.mul.execute([copy.deepcopy(args[1]), div_pol])[0]
        result_polynomial = self.sub.execute([copy.deepcopy(args[0]), mul_for_sub_pol])[0]
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        pass

zero_coef_1 = Rational(Integer(Natural([5]), True), Natural([1])) # -5
first_coef_1 = Rational(Integer(Natural([8])), Natural([1])) # 8
second_coef_1 = Rational(Integer(Natural([3]), True), Natural([1])) # -3
third_coef_1 = Rational(Integer(Natural([4]), True), Natural([1])) # -4
forth_coef_1 = Rational(Integer(Natural([2])), Natural([1])) # 2
fifth_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
sixth_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 1
first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1, forth_coef_1, fifth_coef_1, sixth_coef_1]) # -5+8x-3x^2-4x^3+2x^4+x^6
zero_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
first_coef_2 = Rational(Integer(Natural([1]), True), Natural([1])) # -1
second_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
third_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
forth_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
fifth_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2, forth_coef_2, fifth_coef_2]) # 1-x+x^2+x^5
A = MOD_PP_P()
result = A.execute([second_polym, first_polym])[0]
print(f'\n\n{second_polym} mod \n {first_polym} = \n{result}')