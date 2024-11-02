import unittest
from core.DIV_PP_P import DIV_PP_P
from data_types import *

class DIV_PP_P_test(unittest.TestCase):

    def setUp(self):
        self.module = DIV_PP_P()

    def test_derivative_linear(self):
        coef1 = [
            Rational(Integer(Natural([3])), Natural([1])),  # 3
            Rational(Integer(Natural([2])), Natural([1, 1]))  # 2/11
        ]
        p1 = Polynomial(coef1)   # 2/11x + 3
        coef2 = [
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([2])), Natural([1, 1]))  # 2/11
        ]
        p2 = Polynomial(coef1)  # 2/11x + 1
        coeff = [
            Rational(Integer(Natural([1]), True), Natural([1]))  # 1
        ]
        result = self.module.execute([p1, p2])[0]
        self.assertEqual(result.coefficients, coeff)

    def test_derivative_quadratic(self):
        coef1 = [
            Rational(Integer(Natural([3])), Natural([1])),  # 3
            Rational(Integer(Natural([2])), Natural([1])),  # 2
            Rational(Integer(Natural([1])), Natural([1]))   # 1
        ]
        p1 = Polynomial(coef1)   # x^2 + 2x + 3
        coef2 = [
            Rational(Integer(Natural([2])), Natural([1])),  # 2
            Rational(Integer(Natural([1])), Natural([1]))   # 1
        ]
        p2 = Polynomial(coef2)  # x + 2
        coeff = [
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([1])), Natural([1]))   # 1
        ]
        result = self.module.execute([p1, p2])[0]
        self.assertEqual(result.coefficients, coeff)

    def test_division_with_zero(self):
        coef1 = [
            Rational(Integer(Natural([2])), Natural([1])),  # 2
            Rational(Integer(Natural([1])), Natural([1, 1]))   # 1/11
        ]
        p1 = Polynomial(coef1)   # 1/11x + 2
        coef2 = [
            Rational(Integer(Natural([2])), Natural([1])),  # 2
            Rational(Integer(Natural([1])), Natural([1, 1])),  # 1/11
            Rational(Integer(Natural([1])), Natural([9, 1])),  # 1/19
            Rational(Integer(Natural([9, 6])), Natural([1])),  # 69
            Rational(Integer(Natural([2, 5])), Natural([1]))  # 52
        ]
        p2 = Polynomial(coef2)  # 52x^4 + 69x^3 + 1/19x^2 + 1/11x + 2
        coeff = [
            Rational(Integer(Natural([0])), Natural([1]))  # 0
        ]
        result = self.module.execute([p1, p2])[0]
        self.assertEqual(result.coefficients, coeff)

    if __name__ == '__main__':
        unittest.main()
