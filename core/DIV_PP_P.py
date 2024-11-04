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
            raise ValueError("Invalid data type in DIV_PP_P: must be Polynomial.")
        
        pol1, pol2 = args
        # если степень числителя меньше степени знаменателя
        if self.deg.execute([pol1]) < self.deg.execute([pol2]):
            return [Polynomial([Rational(Integer(Natural([0])), Natural([1]))])]
            
        # если степень числителя больше или равна
        # находим степень k, домножив на которую делитель, получим многочлен той же степени
        k = len(pol1.coefficients) - len(pol2.coefficients)
        result_coefficients = []

        # в цикле делаем как бы деление столбиком 0<=i<=k
        for i in range(k, -1, -1):
            # домножив, получаем нужную степень
            pol_for_mul = self.mul_xk.execute([pol2, Natural([i])])[0]
            # делением старших коэффициентов находим нужный коэффициент частного
            q_for_mul = self.div.execute([pol1.coefficients[-1], pol_for_mul.coefficients[-1]])[0]
            # вставляем коэффициент в начало
            result_coefficients = [q_for_mul] + result_coefficients
            # умножаем делитель нужной степени на коэффициент
            pol_for_sub = self.mul.execute([pol_for_mul, q_for_mul])[0]
            # отнимаем от исходного полученный многочлен
            result_pol = self.sub.execute([pol1, pol_for_sub])[0]
            # если simplify в вычитании поудалял нули, они всё равно нужны в частном
            while len(self.mul_pp.execute([Polynomial(result_coefficients), pol2])[0].coefficients) < len(pol1.coefficients):
                result_coefficients = [Rational(Integer(Natural([0])), Natural([1]))] + result_coefficients
            if len(result_pol.coefficients) < len(pol2.coefficients):
                break
            pol1 = result_pol
            # переходим к следующему, продолжая деление столбиком

        # делаем результат и возвращаем полиномом
        result_polynomial = Polynomial(result_coefficients)
        result_polynomial.simplify()

        return [result_polynomial]

    def reference(self) -> str:
        pass
