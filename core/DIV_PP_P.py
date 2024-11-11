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
from core.RED_Q_Q import RED_Q_Q
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
        self.red = RED_Q_Q()
    
    def execute(self, args):
        # проверка поданных аргументов
        if len(args) != 2:
            raise ValueError("Function DIV_PP_P takes only 2 args.")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type in DIV_PP_P: must be Polynomial.")
        
        dividend, divisor = copy.deepcopy(args[0]), copy.deepcopy(args[1])
        # если степень числителя меньше степени знаменателя
        if len(dividend.coefficients) < len(divisor.coefficients):
            return [Polynomial([Rational(Integer(Natural([0])), Natural([1]))])]
        #коэфиициенты полинома, являющегося результатом деления
        result_coefficients = []
        degree_difference = len(dividend.coefficients) - len(divisor.coefficients)
        #Изначально знаем степень ответа
        for _ in range(degree_difference + 1):
            result_coefficients.append(Rational(Integer(Natural([0])), Natural([1])))
        # цикл пока степень делимого больше или равна степени делителя
        result_degree_counter = len(dividend.coefficients) - len(divisor.coefficients)
        while len(dividend.coefficients) >= len(divisor.coefficients):
            #проверка
            check = len(dividend.coefficients)
            #Считаем разность степеней 
            degree_difference = len(dividend.coefficients) - len(divisor.coefficients)
            #Переводим в список, чтобы можно было подать в Natural()
            degree_digits = list(map(int, str(degree_difference)[::-1]))
            #Умножаем степень делителя на разность
            mult_devisor = self.mul_xk.execute([divisor, Natural(degree_digits)])[0]
            #Находим коэфициент при этой степени
            coefficient_for_mul = self.div.execute([dividend.coefficients[-1], divisor.coefficients[-1]])[0]
            # Сокращаем дробь
            red_coefficient_for_mul = self.red.execute([coefficient_for_mul])[0]
            # Записываем коэфициент в ответ
            result_coefficients[result_degree_counter] = red_coefficient_for_mul
            #Умножаем на коэфициент и находим полином, который нужно вычесть из делимого
            sub_polynom = self.mul.execute([mult_devisor, red_coefficient_for_mul])[0]
            #результат вычитания
            new_dividend = self.sub.execute([dividend, sub_polynom])[0]
            #Передвигаем счётчик на столько единиц, насколько уменьшилась степень
            result_degree_counter -= len(dividend.coefficients) - len(new_dividend.coefficients)
            #Делим полином, полученный в результате вычитания
            dividend = new_dividend
            #обещанная проверка
            if check == 1:
                break
        res_pol = Polynomial(result_coefficients)
        res_pol.simplify()
        return [res_pol]

    def reference(self) -> str:
        return ("Quotient from dividing a polynomial by a polynomial when dividing with remainder [POLYNOMIAL, POLYNOMIAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - dividend\n"
                "\t2: Polynomial - divider\n"
                "Returns:\n"
                "\t1: Polynomial - quotient\n"
                "Author: Anastasia Dorogushina\n")
