import unittest
from data_types import *
from core.FAC_P_Q import FAC_P_Q

class FAC_P_Q_test(unittest.TestCase):
    def setUp(self):
        self.fac_module = FAC_P_Q()
    
    def test_FAC_P_Q(self):
        # Умножение ( 1/3 + 10x + 3/9x^2 + 65/7x^3) 
        zero_coef = Rational(Integer(Natural([1])), Natural([3])) # 1/3
        first_coef = Rational(Integer(Natural([0, 1])), Natural([1])) # 10
        second_coef = Rational(Integer(Natural([3])), Natural([9])) # 3/9
        third_coef = Rational(Integer(Natural([5, 6])), Natural([7])) #65/7
        polynom = Polynomial([zero_coef, first_coef, second_coef, third_coef])
        result = self.fac_module.execute([polynom])[0] # Нахождение НОК НОД ( 1/3 + 10x + 3/9x^2 + 65/7x^3)
        # НОК(3, 1, 9, 7) = 63
        # НОД(1, 10, 3, 65) = 390 
        self.assertEqual([str(result.numerator), str(result.denominator)], ["390", "63"])

    def test_FAC_P_Q_negativ(self):
        # Умножение ( 2/6 - 8/9x + 7/3x^2)
        zero_coef = Rational(Integer(Natural([2])), Natural([6])) # 2/6
        first_coef = Rational(Integer(Natural([8]), True), Natural([9])) # -8/9
        second_coef = Rational(Integer(Natural([7])), Natural([3])) # 7/3
        polynom = Polynomial([zero_coef, first_coef, second_coef])
        result = self.fac_module.execute([polynom])[0]
        # НОК(2, 8, 7) = 56
        # НОД(6, 9, 3) = 18 
        self.assertEqual([str(result.numerator), str(result.denominator)], ["56", "18"])

    def test_FAC_P_Q_invalid_argument(self):
        with self.assertRaises(ValueError):
            self.fac_module.execute(["Hellow Sergei Pozdkov"])

    def test_FAC_P_Q_invalid_argument_number(self):
        polynom1 = Polynomial([Rational(Integer(Natural([1])), Natural([3]))])
        polynom2 = Polynomial([Rational(Integer(Natural([5])), Natural([2]))])
        with self.assertRaises(ValueError):
            self.fac_module.execute([polynom1, polynom2])
    
if __name__ == "__main__":
    unittest.main()
