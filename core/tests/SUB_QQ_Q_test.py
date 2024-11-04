import unittest
from core.SUB_QQ_Q import SUB_QQ_Q
from data_types import Natural, Integer, Rational

class SUB_QQ_Q_test(unittest.TestCase):

    def setUp(self):
        self.module = SUB_QQ_Q()

    def test_simple_subtraction(self):
        # 5/4 - 3/4 = 2/4 = 1/2
        first_rational = Rational(Integer(Natural([5])), Natural([4]))  # 5/4
        second_rational = Rational(Integer(Natural([3])), Natural([4]))  # 3/4
        expected_result = Rational(Integer(Natural([2])), Natural([4]))  # 2/4
        result = self.module.execute([first_rational, second_rational])[0]
        self.assertEqual(result.numerator.natural.numbers, expected_result.numerator.natural.numbers)
        self.assertEqual(result.denominator.numbers, expected_result.denominator.numbers) 

    def test_subtraction_to_zero(self):
        # 7/10 - 7/10 = 0
        first_rational = Rational(Integer(Natural([7])), Natural([0,1]))  # 7/10
        second_rational = Rational(Integer(Natural([7])), Natural([0,1]))  # 7/10
        expected_result = Rational(Integer(Natural([0])), Natural([0,1]))   # 0
        result = self.module.execute([first_rational, second_rational])[0]
        self.assertEqual(result.numerator.natural.numbers, expected_result.numerator.natural.numbers)
        self.assertEqual(result.denominator.numbers, expected_result.denominator.numbers) 

    def test_subtraction_with_negative_result(self):
        # 1/3 - 2/3 = -1/3
        first_rational = Rational(Integer(Natural([1])), Natural([3]))  # 1/3
        second_rational = Rational(Integer(Natural([2])), Natural([3]))  # 2/3
        expected_result = Rational(Integer(Natural([1]), is_positive=False), Natural([3]))  # -1/3
        result = self.module.execute([first_rational, second_rational])[0]
        self.assertEqual(result.numerator.natural.numbers, expected_result.numerator.natural.numbers)
        self.assertEqual(result.numerator.is_positive, expected_result.numerator.is_positive)
        self.assertEqual(result.denominator.numbers, expected_result.denominator.numbers)

    def test_subtraction_with_different_denominators(self):
        # 5/6 - 1/2 = 2/6
        first_rational = Rational(Integer(Natural([5])), Natural([6]))  # 5/6
        second_rational = Rational(Integer(Natural([1])), Natural([2]))  # 1/2
        expected_result = Rational(Integer(Natural([4])), Natural([2,1]))  # 2/6
        result = self.module.execute([first_rational, second_rational])[0]
        self.assertEqual(result.numerator.natural.numbers, expected_result.numerator.natural.numbers)
        self.assertEqual(result.denominator.numbers, expected_result.denominator.numbers)

    def test_invalid_argument_count(self):
        # Неправильное количество аргументов
        rational = Rational(Integer(Natural([5])), Natural([7]))  # 5/7
        with self.assertRaises(ValueError):
            self.module.execute([rational])  # Один аргумент вместо двух
    
    def test_invalid_argument_type(self):
        # Неправильный тип данных аргументов
        rational = Rational(Integer(Natural([5])), Natural([7]))  # 5/7
        invalid_argument = "Invalid argument type"
        with self.assertRaises(ValueError):
            self.module.execute([rational, invalid_argument])  # Второй аргумент не Rational

if __name__ == '__main__':
    unittest.main()
