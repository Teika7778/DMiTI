import unittest
from core.DER_P_P import DER_P_P
from data_types import *

class DER_P_P_test(unittest.TestCase):
    def setUp(self):
        self.module = DER_P_P()

    def test_derivative_constant(self):
        coef = [
            Rational(Integer(Natural([5]), True), Natural([1]))  # 5
        ]
        p = Polynomial(coef)   # 5
        coeff = [
            Rational(Integer(Natural([0]), True), Natural([1]))  # 0
        ]
        result = self.module.execute([p])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

    def test_derivative_linear(self):
        coef = [
            Rational(Integer(Natural([3])), Natural([1])),  # 3
            Rational(Integer(Natural([2])), Natural([1, 1]))  # 2/11
        ]
        p = Polynomial(coef)   # 2/11x + 3
        coeff = [
            Rational(Integer(Natural([2]), True), Natural([1, 1]))  # 2/11
        ]
        result = self.module.execute([p])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

    def test_derivative_quadratic(self):
        coef = [
            Rational(Integer(Natural([1]), True), Natural([1])),  # 1
            Rational(Integer(Natural([2]), True), Natural([1])),  # 2
            Rational(Integer(Natural([3]), False), Natural([2]))  # -3/2
        ]
        p = Polynomial(coef)  # -3/2x^2 + 2x + 1
        coeff = [
            Rational(Integer(Natural([2]), True), Natural([1])),  # 2
            Rational(Integer(Natural([6]), False), Natural([2]))  # -6/2
        ]
        result = self.module.execute([p])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

    def test_derivative_cubic(self):
        coef = [
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([3]), True), Natural([1])),  # 3
            Rational(Integer(Natural([4]), False), Natural([3]))  # -4/3
        ]
        p = Polynomial(coef)  # -4/3x^3 + 3x^2
        coeff = [
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([6]), True), Natural([1])),  # 6
            Rational(Integer(Natural([2, 1]), False), Natural([3]))  # -12/3
        ]
        result = self.module.execute([p])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

    def test_derivative_zero_polynomial(self):
        coef = [
            Rational(Integer(Natural([0]), True), Natural([1]))  # 0
        ]
        p = Polynomial(coef)  # 0
        coeff = [
            Rational(Integer(Natural([0]), True), Natural([1]))  # 0
        ]
        result = self.module.execute([p])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

if __name__ == '__main__':
    unittest.main()
