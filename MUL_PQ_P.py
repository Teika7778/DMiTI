from core import generic_module as gm
from data_types import *
import copy


class MUL_PQ_P(gm.AbstractModule):
    def execute(self, args):
        # Проверка количества аргументов
        if len(args) != 2:
            raise ValueError("Function requires exactly 2 arguments: Polynomial and Rational.")

        polynomial, rational = args

        # Проверка типов аргументов
        if not isinstance(polynomial, Polynomial):
            raise ValueError("First argument must be a Polynomial.")
        if not isinstance(rational, Rational):
            raise ValueError("Second argument must be a Rational number.")

        # Умножаем каждый коэффициент многочлена на рациональное число
        new_coefficients = [
            Rational(
                Integer(copy.deepcopy(coef.numerator.natural)),
                copy.deepcopy(coef.denominator)
            )
            for coef in polynomial.coefficients
        ]

        # Создаем новый многочлен с обновленными коэффициентами
        result_polynomial = Polynomial(new_coefficients)

        return [result_polynomial]  # Возвращаем результат в виде массива

    def reference(self) -> str:
        return "MUL_PQ_P - Multiplies each coefficient of a polynomial by a rational number."
