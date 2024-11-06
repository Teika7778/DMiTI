from core import generic_module as gm
# деление дробей
from core.DIV_QQ_Q import DIV_QQ_Q
# степень многочлена
from core.DEG_P_N import DEG_P_N
# умножение многочлена на x^k, k>=0
from core.MUL_Pxk_P import MUL_Pxk_P
# умножение многочлена на дробь
from core.MUL_PQ_P import MUL_PQ_P
# вычитание многочленов
from core.MUL_PP_P import MUL_PP_P
from core.SUB_PP_P import SUB_PP_P
# сложение многочленов хоть и есть в зависимостях, не используется
from data_types import *
import copy

class DIV_PP_P(gm.AbstractModule):
    # добавляем функции, которыми пользуемся
    def __init__(self):
        self.mul_pp = MUL_PP_P()
        self.div = DIV_QQ_Q()
        self.deg = DEG_P_N()
        self.mul_xk = MUL_Pxk_P()
        self.mul = MUL_PQ_P()
        self.sub = SUB_PP_P()
    
    def execute(self, args):
        # проверка поданных аргументов
        if len(args) != 2:
            raise ValueError("Function DIV_PP_P takes only 2 args.")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type in DIV_PP_P: must be Polynomial .")
        
        dividend, divisor = copy.deepcopy(args[0]), copy.deepcopy(args[1])
        # если степень числителя меньше степени знаменателя
        if len(dividend.coefficients) < len(divisor.coefficients):
            return [Polynomial([Rational(Integer(Natural([0])), Natural([1]))])]
        
        result_coefficients = []

        while len(dividend.coefficients) >= len(divisor.coefficients):
            degree_difference = len(dividend.coefficients) - len(divisor.coefficients)
            degree_digits = list(map(int, str(degree_difference)[::-1]))
            mult_devisor = self.mul_xk.execute([divisor, Natural(degree_digits)])[0]
            coefficient_for_mul = self.div.execute([dividend.coefficients[-1], divisor.coefficients[-1]])[0]
            result_coefficients = [coefficient_for_mul] + result_coefficients
            sub_polynom = self.mul.execute([mult_devisor, coefficient_for_mul])[0]
            new_dividend = self.sub.execute([dividend, sub_polynom])[0]
            print(f'({dividend}) - ({sub_polynom}) = ({new_dividend}), {len(new_dividend.coefficients)}\n')
            if ((len(dividend.coefficients) - len(new_dividend.coefficients)) >= 2 and  list(map(str, new_dividend.coefficients)) != ['0']):
                for _ in range(len(dividend.coefficients) - len(new_dividend.coefficients) -1):
                    result_coefficients = [Rational(Integer(Natural([0])), Natural([1]))] + result_coefficients
            dividend = new_dividend
            
        return [Polynomial(result_coefficients)]
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
A = DIV_PP_P()
result = A.execute([second_polym, first_polym])[0]
print(f'\n\n{second_polym} / \n {first_polym} = \n{result}')