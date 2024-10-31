import unittest
from core.SUB_PP_P import SUB_PP_P
from data_types import *

class SUB_PP_P_test(unittest.TestCase):

    def setUp(self):
        self.module = SUB_PP_P()

    def test_subtract_polynomials(self):
        # создаем полиномы p1 и p2
        coef1 = [
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([2])), Natural([1])),  # 2
            Rational(Integer(Natural([3])), Natural([1]))  # 3
        ]
        P1 = Polynomial(coef1)

        coef2 = [
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([1])), Natural([1])),  # 1
        ]
        P2 = Polynomial(coef2)

        expected_coef = [
            Rational(Integer(Natural([1])), Natural([1])),  # 0
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([2])), Natural([1]))  # 3
        ]
        expected_result = Polynomial(expected_coef)     # 12
        result = self.module.execute([P1, P2])
        self.assertEqual(result.str(), expected_result.str())

    def test_subtract_polynomials_with_zero_result(self):
        coef3 = [
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([0])), Natural([1]))  # 0
        ]
        P3 = Polynomial(coef3)

        coef4 = [
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([0])), Natural([1]))  # 0
        ]
        P4 = Polynomial(coef4)
        expected_zero_poly = Polynomial([0])  # 0
        result = self.sub_pp.execute([P3, P4])
        self.assertEqual(result.str(), expected_zero_poly.str())

    if __name__ == "__main__":
        unittest.main()
