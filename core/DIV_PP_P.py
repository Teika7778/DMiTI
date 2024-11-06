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

class DIV_PP_P_new(gm.AbstractModule):
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
            if ((len(dividend.coefficients) - len(new_dividend.coefficients)) >= 2 and  list(map(str, new_dividend.coefficients)) != ['0']):
                for _ in range(len(dividend.coefficients) - len(new_dividend.coefficients) -1):
                    result_coefficients = [Rational(Integer(Natural([0])), Natural([1]))] + result_coefficients
            dividend = new_dividend
            
        return [Polynomial(result_coefficients)]
    def reference(self) -> str:
        pass