import unittest
from data_types import *
from core.GCF_PP_P import GCF_PP_P


class GCF_PP_P_test(unittest.TestCase):
    def setUp(self):
        self.gcf_module = GCF_PP_P()

    def test_GCF(self):
        zero_coef_1 = Rational(Integer(Natural([5]), True), Natural([1])) # -5
        first_coef_1 = Rational(Integer(Natural([8])), Natural([1])) # 8
        second_coef_1 = Rational(Integer(Natural([3]), True), Natural([1])) # -3
        third_coef_1 = Rational(Integer(Natural([4]), True), Natural([1])) # -4
        forth_coef_1 = Rational(Integer(Natural([2])), Natural([1])) # 2
        fifth_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
        sixth_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 1
        first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1, forth_coef_1, fifth_coef_1, sixth_coef_1]) # -5+8x-3x^2-4x^3+2x^4+x^6
        zero_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
        first_coef_2 = Rational(Integer(Natural([1]), True), Natural([1])) # -1
        second_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
        third_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
        forth_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
        fifth_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
        second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2, forth_coef_2, fifth_coef_2]) # 1-x+x^2+x^5
        result = self.gcf_module.execute([first_polym, second_polym])[0]
        #1-x+x^3
        correct_answer = Polynomial(Rational(Integer(Natural([1])), Natural([1])), Rational(Integer(Natural([1]), True), Natural([1])), Rational(Integer(Natural([0])), Natural([1])), Rational(Integer(Natural([1])), Natural([1])))
        self.assertEqual([str(elem) for elem in result.coefficients], [str(elem) for elem in correct_answer.coefficients])

    def test_GCF(self):
        zero_coef_1 = Rational(Integer(Natural([1]), True), Natural([1])) # -1
        first_coef_1 = Rational(Integer(Natural([4]), True), Natural([1])) # -4
        second_coef_1 = Rational(Integer(Natural([3]), True), Natural([1])) # -3
        third_coef_1 = Rational(Integer(Natural([1])), Natural([1])) # 1
        forth_coef_1 = Rational(Integer(Natural([1])), Natural([1])) # 1
        first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1, forth_coef_1]) # -1-4x-3x^2+x^3+x^4
        zero_coef_2 = Rational(Integer(Natural([1]), True), Natural([1])) # -1
        first_coef_2 = Rational(Integer(Natural([1]), True), Natural([1])) # -1
        second_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
        third_coef_2 = Rational(Integer(Natural([1])), Natural([1])) # 1
        second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2]) #-1-x+x^2+x^3
        result = self.gcf_module.execute([first_polym, second_polym])[0]
        #-x-1
        correct_answer = Polynomial(Rational(Integer(Natural([1]), True), Natural([1])), Rational(Integer(Natural([1]), True), Natural([1])) )
        self.assertEqual([str(elem) for elem in result.coefficients], [str(elem) for elem in correct_answer.coefficients])

