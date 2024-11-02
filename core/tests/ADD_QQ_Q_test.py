import unittest
from core.ADD_QQ_Q import ADD_QQ_Q
from data_types import Natural, Integer, Rational


class ADD_QQ_Q_test(unittest.TestCase):
    def setUp(self):
        self.add_module = ADD_QQ_Q()

    def test_add_positive_fractions(self):
        # Сложение 3/4 + 5/6 = 19/12
        first_rational = Rational(Integer(Natural([3])), Natural([4]))  # 3/4
        second_rational = Rational(Integer(Natural([5])), Natural([6]))  # 5/6
        result = self.add_module.execute([first_rational, second_rational])[0]
        self.assertEqual(
            [str(result.numerator), str(result.denominator)],
            [str(Integer(Natural([9, 1]))), str(Natural([2, 1]))]
        )

    def test_add_negative_fraction(self):
        # Сложение -7/10 + 3/5 = -1/2
        first_rational = Rational(Integer(Natural([7]), False), Natural([10]))  # -7/10
        second_rational = Rational(Integer(Natural([3])), Natural([5]))         # 3/5
        result = self.add_module.execute([first_rational, second_rational])[0]
        self.assertEqual(
            [str(result.numerator), str(result.denominator)],
            [str(Integer(Natural([1]), False)), str(Natural([2]))]
        )

    def test_add_zero_fraction(self):
        # Сложение 0/1 + 4/5 = 4/5
        first_rational = Rational(Integer(Natural([0])), Natural([1]))  # 0
        second_rational = Rational(Integer(Natural([4])), Natural([5]))  # 4/5
        result = self.add_module.execute([first_rational, second_rational])[0]
        self.assertEqual(
            [str(result.numerator), str(result.denominator)],
            [str(Integer(Natural([4]))), str(Natural([5]))]
        )

    def test_add_same_denominator(self):
        # Сложение 7/8 + 3/8 = 10/8
        first_rational = Rational(Integer(Natural([7])), Natural([8]))  # 7/8
        second_rational = Rational(Integer(Natural([3])), Natural([8])) # 3/8
        result = self.add_module.execute([first_rational, second_rational])[0]
        self.assertEqual(
            [str(result.numerator), str(result.denominator)],
            [str(Integer(Natural([0, 1]))), str(Natural([8]))]
        )

    def test_invalid_argument_count(self):
        # Неправильное количество аргументов (ожидается ошибка)
        rational = Rational(Integer(Natural([5])), Natural([7]))  # 5/7
        with self.assertRaises(ValueError):
            self.add_module.execute([rational])  # Один аргумент вместо двух

    def test_invalid_argument_type(self):
        # Проверка, если тип аргумента неверный (ожидается ошибка)
        rational = Rational(Integer(Natural([5])), Natural([7]))  # 5/7
        invalid_argument = "Invalid argument type"
        with self.assertRaises(ValueError):
            self.add_module.execute([rational, invalid_argument])  # Второй аргумент не Rational

if __name__ == '__main__':
    unittest.main()
