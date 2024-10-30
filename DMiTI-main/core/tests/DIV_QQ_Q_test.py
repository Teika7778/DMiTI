import unittest
from data_types import *
from core.DIV_QQ_Q import DIV_QQ_Q


class TRANS_Q_Z_test(unittest.TestCase):
    def test_num_valid(self):
        module = DIV_QQ_Q()
        rational1 = Rational(Integer(Natural([2]), is_positive = True), Natural([3]))
        rational2 = Rational(Integer(Natural([4]), is_positive = True), Natural([5]))
        mustRational = Rational(Integer(Natural([0,1]), is_positive = True), Natural([2,1]))
        result = module.execute([rational1, rational2])
        self.assertEqual(result[0].numerator.natural.numbers,mustRational.numerator.natural.numbers) # проверяем знамянатели полученного значения
    
    def test_denum_valid(self):
        module = DIV_QQ_Q()
        rational1 = Rational(Integer(Natural([2]), is_positive = True), Natural([3]))
        rational2 = Rational(Integer(Natural([4]), is_positive = True), Natural([5]))
        mustRational = Rational(Integer(Natural([0,1]), is_positive = True), Natural([2,1]))
        result = module.execute([rational1, rational2])
        self.assertEqual(result[0].denominator.numbers,mustRational.denominator.numbers)  # Проверяем числители полученного значения

    def test_non_two_positive_type(self):
        module = DIV_QQ_Q()
        rational1 = Rational(Integer(Natural([2]), is_positive = False), Natural([3]))
        rational2 = Rational(Integer(Natural([4]), is_positive = False), Natural([5]))
        result = module.execute([rational1, rational2])
        self.assertEqual(result[0].numerator.is_positive , True)  # Проверяем знак результата 

    def test_non_and_positive_type(self):
        module = DIV_QQ_Q()
        rational1 = Rational(Integer(Natural([2]), is_positive = False), Natural([3]))
        rational2 = Rational(Integer(Natural([4]), is_positive = True), Natural([5]))
        result = module.execute([rational1, rational2])
        self.assertEqual(result[0].numerator.is_positive ,False)   # Проверяем знак результата 
   

if __name__ == '__main__':
    unittest.main()