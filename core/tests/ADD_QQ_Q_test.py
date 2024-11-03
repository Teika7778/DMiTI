import unittest
from data_types import Rational, Natural
from core.ADD_QQ_Q import ADD_QQ_Q  # Импортируем класс ADD_QQ_Q

class TestADDQQQ(unittest.TestCase):

    def setUp(self):
        self.add_qq_q = ADD_QQ_Q()  # Создаем экземпляр нашего модуля

    def test_add_positive_rationals(self):
        # Тест сложения положительных дробей
        r1 = Rational(Natural([1]), Natural([2]))  # 1/2
        r2 = Rational(Natural([1]), Natural([3]))  # 1/3
        result = self.add_qq_q.execute([r1, r2])
        self.assertEqual(result[0].numerator.numbers, [5])  # 5 (числитель)
        self.assertEqual(result[0].denominator.numbers, [6])  # 6 (знаменатель), т.к. 1/2 + 1/3 = 5/6

    def test_add_negative_rationals(self):
        # Тест сложения отрицательных дробей
        r1 = Rational(Natural([1]), Natural([2]))  # 1/2
        r2 = Rational(Natural([1]), Natural([3]))  # 1/3
        result = self.add_qq_q.execute([-r1, -r2])
        self.assertEqual(result[0].numerator.numbers, [-5])  # -5 (числитель)
        self.assertEqual(result[0].denominator.numbers, [6])  # 6 (знаменатель)

    def test_add_mixed_rationals(self):
        # Тест сложения смешанных дробей
        r1 = Rational(Natural([1]), Natural([2]))  # 1/2
        r2 = Rational(Natural([2]), Natural([3]))  # 2/3
        result = self.add_qq_q.execute([r1, r2])
        self.assertEqual(result[0].numerator.numbers, [7])  # 7 (числитель)
        self.assertEqual(result[0].denominator.numbers, [6])  # 6 (знаменатель), т.к. 1/2 + 2/3 = 7/6

    def test_add_zero_rational(self):
        # Тест сложения дроби с нулем
        r1 = Rational(Natural([1]), Natural([2]))  # 1/2
        r2 = Rational(Natural([0]), Natural([1]))  # 0/1 (ноль)
        result = self.add_qq_q.execute([r1, r2])
        self.assertEqual(result[0].numerator.numbers, [1])  # 1 (числитель)
        self.assertEqual(result[0].denominator.numbers, [2])  # 2 (знаменатель)

    def test_invalid_arguments(self):
        # Тест на неправильные аргументы
        with self.assertRaises(ValueError):
            self.add_qq_q.execute([Rational(Natural([1]), Natural([2]))])  # Одного аргумента
        with self.assertRaises(ValueError):
            self.add_qq_q.execute([1, 2])  # Неправильные типы данных

if __name__ == '__main__':
    unittest.main()
