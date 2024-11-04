import unittest
from data_types import *
from core.MUL_PP_P import MUL_PP_P
from core.MUL_Pxk_P import MUL_Pxk_P

class MUL_PP_P_test(unittest.TestCase):
    def setUp(self):
        self.mul_module = MUL_PP_P()
        self.mul_px = MUL_Pxk_P()
    
    def test_multiplication(self):
        # Умножение (x + x^3)*(5x+3^3)
        zero_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0 
        first_coef_1 = Rational(Integer(Natural([1])), Natural([1])) # x
        second_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef_1 = Rational(Integer(Natural([1])), Natural([1])) #x^3
        first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1])
        zero_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0 
        first_coef_2 = Rational(Integer(Natural([5])), Natural([1])) # 5x
        second_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef_2 = Rational(Integer(Natural([3])), Natural([1])) #3x^3
        second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2])
        result = self.mul_module.execute([first_polym, second_polym]) # Умножение (x + x^3)*(5x+3^3)
        zero_coef_3 = Rational(Integer(Natural([0])), Natural([1])) # 0 
        first_coef_3 = Rational(Integer(Natural([0])), Natural([1])) # 0
        second_coef_3 = Rational(Integer(Natural([5])), Natural([1])) # 5x^2
        third_coef_3 = Rational(Integer(Natural([0])), Natural([1])) #0
        forth_coef_3 = Rational(Integer(Natural([8])), Natural([1])) #8x^4
        fifth_coef_3 = Rational(Integer(Natural([0])), Natural([1])) #0
        sixth_coef_3 = Rational(Integer(Natural([3])), Natural([1])) #3x^6
        # 5x^2 + 8x^4 + 3x^6
        correct_answer = Polynomial([zero_coef_3, first_coef_3, second_coef_3, third_coef_3, forth_coef_3, fifth_coef_3, sixth_coef_3])
        self.assertEqual([str(elem) for elem in correct_answer.coefficients], [str(elem) for elem in result[0].coefficients])

    def test_multiplication_big(self):
        # Умножение (x + x^3)*(5x+3^3)*x^9*x^9
        zero_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
        first_coef_1 = Rational(Integer(Natural([1])), Natural([1])) # x
        second_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef_1 = Rational(Integer(Natural([1])), Natural([1])) #x^3
        first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1])
        zero_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
        first_coef_2 = Rational(Integer(Natural([5])), Natural([1])) # 5x
        second_coef_2 = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef_2 = Rational(Integer(Natural([3])), Natural([1])) #3x^3
        second_polym = Polynomial([zero_coef_2, first_coef_2, second_coef_2, third_coef_2])
        first_polym = self.mul_px.execute([first_polym, Natural([9])])[0]
        second_polym = self.mul_px.execute([second_polym, Natural([9])])[0]
        result = self.mul_module.execute([first_polym, second_polym]) # Умножение (x + x^3)*(5x+3^3)
        zero_coef_3 = Rational(Integer(Natural([0])), Natural([1])) # 0
        first_coef_3 = Rational(Integer(Natural([0])), Natural([1])) # 0
        second_coef_3 = Rational(Integer(Natural([5])), Natural([1])) # 5x^2
        third_coef_3 = Rational(Integer(Natural([0])), Natural([1])) #0
        forth_coef_3 = Rational(Integer(Natural([8])), Natural([1])) #8x^4
        fifth_coef_3 = Rational(Integer(Natural([0])), Natural([1])) #0
        sixth_coef_3 = Rational(Integer(Natural([3])), Natural([1])) #3x^6
        # 5x^2 + 8x^4 + 3x^6
        correct_answer = Polynomial([zero_coef_3, first_coef_3, second_coef_3, third_coef_3, forth_coef_3, fifth_coef_3, sixth_coef_3])
        correct_answer = self.mul_px.execute([correct_answer, Natural([8, 1])])[0]
        self.assertEqual([str(elem) for elem in correct_answer.coefficients], [str(elem) for elem in result[0].coefficients])
    def test_invalid_argument(self):
        # Неправильный аргумент
        zero_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0 
        first_coef_1 = Rational(Integer(Natural([1])), Natural([1])) # x
        second_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef_1 = Rational(Integer(Natural([1])), Natural([1])) #x^3
        first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1])
        with self.assertRaises(ValueError):
            self.mul_module([first_polym, "Hellow Sergei Pozdkov"])

    def test_invalid_argument(self):
        # Неправильное число аргументов
        zero_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0 
        first_coef_1 = Rational(Integer(Natural([1])), Natural([1])) # x
        second_coef_1 = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef_1 = Rational(Integer(Natural([1])), Natural([1])) #x^3
        first_polym = Polynomial([zero_coef_1, first_coef_1, second_coef_1, third_coef_1])
        with self.assertRaises(ValueError):
            self.mul_module.execute([first_polym])

if __name__ == "__main__":
    unittest.main()
