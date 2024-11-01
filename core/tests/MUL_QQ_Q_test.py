import unittest
from data_types import *
from core.MUL_QQ_Q import MUL_QQ_Q


class Mul_QQ_Q(unittest.TestCase):
    def setUp(self):
        self.mul_module = MUL_QQ_Q()

    def test_positive_multiplication(self):
        # 12/10 * 100/2
        first_numerator = Integer(Natural([2, 1])) # 12
        first_denominator = Natural([0, 1]) # 10
        first_rational = Rational(first_numerator, first_denominator) # 12/10
        second_numerator = Integer(Natural([0, 0, 1])) # 100
        second_denominator = Natural([2]) # 2
        second_rational = Rational(second_numerator, second_denominator) #100/2
        result = self.mul_module.execute([first_rational, second_rational]) # 1200/20
        self.assertEqual([str(result[0].numerator), str(result[0].denominator)], [str(Integer(Natural([0, 0, 2, 1]))), str(Natural([0, 2]))])

    def test_negativ_multiplication(self):
        # -22/3 * 2/3
        first_numerator = Integer(Natural([2, 2]), False) # 22
        first_denominator = Natural([3]) # 3
        first_rational = Rational(first_numerator, first_denominator) # -22/3
        second_numerator = Integer(Natural([2])) # 2
        second_denominator = Natural([3]) # 3
        second_rational = Rational(second_numerator, second_denominator) #2/3
        result = self.mul_module.execute([first_rational, second_rational]) # -44/9
        self.assertEqual([str(result[0].numerator), str(result[0].denominator)], [str(Integer(Natural([4, 4]), False)), str(Natural([9]))])

    def test_zero_multiplication(self):
        # 5/7 * 0
        first_numerator = Integer(Natural([5])) # 5
        first_denominator = Natural([7]) # 7
        first_rational = Rational(first_numerator, first_denominator) # 5/7
        second_numerator = Integer(Natural([0])) # 0
        second_denominator = Natural([1]) # 1
        second_rational = Rational(second_numerator, second_denominator) #0
        result = self.mul_module.execute([first_rational, second_rational]) # 0
        self.assertEqual([str(result[0].numerator), str(result[0].denominator)], [str(Integer(Natural([0]), False)), str(Natural([7]))]) # ?? 

    def test_million_multiplication(self):
        # 1000000/1627 * 3/4
        first_numerator = Integer(Natural([0, 0, 0, 0, 0, 0, 1])) # 1000000
        first_denominator = Natural([7, 2, 6, 1]) # 1627
        first_rational = Rational(first_numerator, first_denominator) # 1000000/1627
        second_numerator = Integer(Natural([3])) # 3
        second_denominator = Natural([4]) # 4
        second_rational = Rational(second_numerator, second_denominator) #3/4
        result = self.mul_module.execute([first_rational, second_rational]) #3000000/6508
        self.assertEqual([str(result[0].numerator), str(result[0].denominator)], [str(Integer(Natural([0, 0, 0, 0, 0, 0, 3]))), str(Natural([8, 0, 5, 6]))])

    def test_invalid_argument_count(self):
        # Неправильное число аргументов
        first_numerator = Integer(Natural([5])) # 5
        first_denominator = Natural([7]) # 7
        first_rational = Rational(first_numerator, first_denominator) # 5/7
        with self.assertRaises(ValueError):
            self.mul_module.execute([first_rational]) # один аргумент

    def test_invalid_argument_type(self):
        # Проверка на неправильное число аргументов
        first_numerator = Integer(Natural([5])) # 5
        first_denominator = Natural([7]) # 7
        first_rational = Rational(first_numerator, first_denominator) # 5/7
        invalid_argument = "Hellow  Sergey Pozdkov"
        with self.assertRaises(ValueError):
            self.mul_module.execute([first_rational, invalid_argument]) # неправильный аргумент  

if __name__ == "__main__":
    unittest.main()
