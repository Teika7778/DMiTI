import unittest
from core.NMR_P_P import NMR_P_P
from data_types import *

class NMR_P_P_test(unittest.TestCase):

    def setUp(self):
        self.module = NMR_P_P()

    def test_derivative_quadratic(self):
        coef = [
            Rational(Integer(Natural([9]), True), Natural([1])),  # 9
            Rational(Integer(Natural([1]), False), Natural([1])),  # -1
            Rational(Integer(Natural([1]), True), Natural([9]))  # 1/9
        ]
        p = Polynomial(coef)   # (1/3x-3)^2
        coeff = [
            Rational(Integer(Natural([3]), False), Natural([1])),  # -3
            Rational(Integer(Natural([1]), True), Natural([3]))  # 1/3
        ]
        result = self.module.execute([p])    # 1/3x-3
        self.assertEqual(result.coefficients, coeff)

    def test_derivative_linear(self):
        coef = [
            Rational(Integer(Natural([9]), True), Natural([1])),  # 9
            Rational(Integer(Natural([1]), False), Natural([988]))  # -1/988
        ]
        p = Polynomial(coef)  # -1/988x+9
        coeff = [
            Rational(Integer(Natural([9]), True), Natural([1])),  # 9
            Rational(Integer(Natural([1]), False), Natural([988]))  # -1/988
        ]
        result = self.module.execute([p])  # -1/988x+9
        self.assertEqual(result.coefficients, coeff)

    def test_division_with_zero(self):
        coef = [
            Rational(Integer(Natural([9]), True), Natural([21]))  # 9/21
        ]
        p = Polynomial(coef)  # 9/21
        coeff = [
            Rational(Integer(Natural([9]), True), Natural([21]))  # 9/21
        ]
        result = self.module.execute([p])  # 9/21
        self.assertEqual(result.coefficients, coeff)

    if __name__ == '__main__':
        unittest.main()
