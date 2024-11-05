import unittest
from core.SUB_PP_P import SUB_PP_P
from data_types import *

class SUB_PP_P_test(unittest.TestCase):

    def setUp(self):
        self.module = SUB_PP_P()

    def test_subtract_polynomials(self):
        # создаем полиномы p1 и p2
        coef1 = [
            Rational(Integer(Natural([1]), True), Natural([1])),  # 1
            Rational(Integer(Natural([2]), True), Natural([1])),  # 2
            Rational(Integer(Natural([3]), True), Natural([1]))  # 3
        ]
        P1 = Polynomial(coef1)

        coef2 = [
            Rational(Integer(Natural([1]), True), Natural([1])),  # 1
            Rational(Integer(Natural([1]), True), Natural([1])),  # 1
        ]
        P2 = Polynomial(coef2)

        expected_coef = [
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([1]), True), Natural([1])),  # 1
            Rational(Integer(Natural([3]), True), Natural([1]))  # 3
        ]
        expected_result = Polynomial(expected_coef)     # 310
        result = self.module.execute([P1, P2])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in expected_coef])

    def test_subtract_polynomials_with_zero_result(self):
        coef3 = [
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([0]), True), Natural([1]))  # 0
        ]
        P3 = Polynomial(coef3)

        coef4 = [
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([0]), True), Natural([1])),  # 0
            Rational(Integer(Natural([0]), True), Natural([1]))  # 0
        ]
        P4 = Polynomial(coef4)

        coeff = [
            Rational(Integer(Natural([0]), True), Natural([1]))  #0
        ]
        expected_zero_poly = Polynomial(coeff)  # 0
        result = self.module.execute([P3, P4])[0]
        self.assertEqual([str(coef) for coef in result.coefficients],
                         [str(coef) for coef in coeff])

if __name__ == "__main__":
    unittest.main()
