from core import generic_module as gm
from data_types import *
from core.MUL_QQ_Q import MUL_QQ_Q

class MUL_PQ_P(gm.AbstractModule):
    def __init__(self):
        self.mul_qq_q = MUL_QQ_Q()  # Экземпляр для умножения рациональных чисел

    def execute(self, args):
        # Проверка на наличие двух аргументов
        if len(args) != 2:
            raise ValueError("Improper arguments: function takes 2 args")
        polynomial, rational = args
        # Проверка типа данных
        if not (isinstance(polynomial, Polynomial) and isinstance(rational, Rational)):
            raise ValueError("Invalid data types: expected Polynomial and Rational")

        # Умножение каждого коэффициента многочлена на рациональное число
        new_coefficients = [
            self.mul_qq_q.execute([coef, rational])[0]
            for coef in polynomial.coefficients
        ]
        
        # Создаем новый многочлен с обновленными коэффициентами
        result_polynomial = Polynomial(new_coefficients)
        result_polynomial.simplify()
        return [result_polynomial]  # Возвращаем как массив

    def reference(self) -> str:
        return ("Multiplication of a polynomial by a fractional [POLYNOMIAL. RATIONAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - multiplier\n"
                "\t2: Rational - multiplicand\n"
                "Returns:\n"
                "\t1: Polynomial - product of multiplication\n"
                "Author: Erdni Baatyrov\n")
