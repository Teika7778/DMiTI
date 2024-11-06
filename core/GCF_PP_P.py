from core import generic_module as gm
from data_types import *
from core.MOD_PP_P import MOD_PP_P
import copy


class GCF_PP_P(gm.AbstractModule):
    def __init__(self):
        self.mod_pp_p = MOD_PP_P()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type:  must be polynomial")
        arg0_copy = copy.deepcopy(args[0])  # Копии многочленов
        arg1_copy = copy.deepcopy(args[1])
        # Алгоритм Евклида делением
        # Пока степени обоих не равны нулю
        while len(arg0_copy.coefficients) > 1 and len(arg1_copy.coefficients) > 1:
            print(arg0_copy, '\t',  arg1_copy)
            # если степень первого больше
            if len(arg0_copy.coefficients) > len(arg1_copy.coefficients):
                # делим на второй
                arg0_copy = self.mod_pp_p.execute([arg0_copy, arg1_copy])[0]
            else:  # иначе
                arg1_copy = self.mod_pp_p.execute([arg1_copy, arg0_copy])[0]  # делим на первый

        if len(arg0_copy.coefficients) == 1:  # проверяем, какой не равен нулю
            return [arg1_copy]
        else:
            return [arg0_copy]

    def reference(self) -> str:
        pass

zero_coef_1 = Rational(Integer(Natural([5]), True), Natural([1])) # -5
first_coef_1 = Rational(Integer(Natural([8])), Natural([1])) # 8
second_coef_1 = Rational(Integer(Natural([3]), True), Natural([1])) # -3
third_coef_1 = Rational(Integer(Natural([4]), True), Natural([1])) # -4
forth_coef_1 = Rational(Integer(Natural([2])), Natural([1])) # 2
first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1, forth_coef_1]) # -5+8x-3x^2-4x^3+2x^4+x^6
zero_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
first_coef_2 = Rational(Integer(Natural([1]), True), Natural([1])) # -1
second_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
third_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
forth_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
fifth_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2, forth_coef_2, fifth_coef_2]) # 1-x+x^2+x^5
A = GCF_PP_P()
result = A.execute([first_polym, second_polym])[0]
#1-x+x^3
correct_answer = Polynomial([Rational(Integer(Natural([1])), Natural([1])), 
    Rational(Integer(Natural([1])), Natural([1])), 
    Rational(Integer(Natural([0])), Natural([1])), 
    Rational(Integer(Natural([1])), Natural([1]))])

print(result)
print(correct_answer)