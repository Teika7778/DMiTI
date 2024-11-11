import unittest
from core.NMR_P_P import NMR_P_P
from data_types import *

class NMR_P_P_test(unittest.TestCase):

    def setUp(self):
        self.module = NMR_P_P()

    def test_derivative_quadratic(self):
        coef = [
            Rational(Integer(Natural([1]), True), Natural([1])),  # 1
            Rational(Integer(Natural([6]), True), Natural([1])),  # 6
            Rational(Integer(Natural([9]), True), Natural([1]))  # 9
        ]
        p = Polynomial(coef)   # (3x+1)^2
        coeff = [
            Rational(Integer(Natural([1]), True), Natural([6])),  # 1
            Rational(Integer(Natural([1]), True), Natural([2]))  # 3
        ]
        result = self.module.execute([p])[0]    # 3x+1
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

    def test_derivative_linear(self):
        coef = [
            Rational(Integer(Natural([9]), True), Natural([1])),  # 9
            Rational(Integer(Natural([1]), False), Natural([8, 8, 9]))  # -1/988
        ]
        p = Polynomial(coef)  # -1/988x+9
        coeff = [
            Rational(Integer(Natural([9]), True), Natural([1])),  # 9
            Rational(Integer(Natural([1]), False), Natural([8, 8, 9]))  # -1/988
        ]
        result = self.module.execute([p])[0]  # -1/988x+9
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

    def test_division_with_zero(self):
        coef = [
            Rational(Integer(Natural([9]), True), Natural([1, 2]))  # 9/21
        ]
        p = Polynomial(coef)  # 9/21
        coeff = [
            Rational(Integer(Natural([3]), True), Natural([7]))  # 9/21
        ]
        result = self.module.execute([p])[0]  # 9/21
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

if __name__ == '__main__':
    unittest.main()
