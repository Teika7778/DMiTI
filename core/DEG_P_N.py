from core import generic_module as gm
from data_types import *
import copy


class DEG_P_N(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 1:  # Проверка на получение единственного аргумента
            raise ValueError("Improper arguments: function takes only 1 arg")
        
        polynomial = copy.deepcopy(args[0])
        
        if not isinstance(polynomial, Polynomial):  # Проверка типа
            raise ValueError("Invalid data type: must be polynomial")
        
        # Удаление незначащих нулей перед вычислением степени
        polynomial.simplify()
        
        # Определение степени как длина массива коэффициентов - 1
        degree = len(polynomial.coefficients) - 1
        degree = list(map(int, list(str(degree))[::-1]))
        return [Natural(degree)]  # Возвращаем массив с единственным элементом — степенью многочлена
    
    def reference(self) -> str:
        return "DEG_P_N - Determines the degree of a polynomial."
