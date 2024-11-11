from core import generic_module as gm
from data_types import *
import copy


class LED_P_Q(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 1:  # Проверка на получение единственного аргумента
            raise ValueError("Improper arguments: function takes only 1 arg")

        polynomial = copy.deepcopy(args[0])

        if not isinstance(polynomial, Polynomial):  # Проверка типа
            raise ValueError("Invalid data type: must be polynomial")

        polynomial.simplify()  # Удаление незначащих нулей

        # Старший коэффициент — последний элемент списка после упрощения
        lead_coeff = polynomial.coefficients[-1]

        return [lead_coeff]  # Возвращаем массив с одним элементом - старшим коэффициентом

    def reference(self) -> str:
        return ("Senior coefficient of the polynomial [POLYNOMIAL -> RATIONAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - original\n"
                "Returns:\n"
                "\t1: Rational - senior coefficient\n"
                "Author: Erdni Baatyrov\n")
