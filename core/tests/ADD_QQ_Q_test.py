import unittest
from data_types import *
from core.ADD_QQ_Q import ADD_QQ_Q  # Импортируем класс ADD_QQ_Q

class TestADDQQQ(unittest.TestCase):

    def setUp(self):
        self.add_qq_q = ADD_QQ_Q()  # Создаем экземпляр нашего модуля

    def test_add_positive_rationals(self):
        # Тест сложения положительных дробей
        r1 = Rational(Integer(Natural([1]), True), Natural([2]))  # 1/2
        r2 = Rational(Integer(Natural([1]), True), Natural([3]))  # 1/3
        result = self.add_qq_q.execute([r1, r2])[0]
        num = Integer(Natural([5]), True)
        den = Natural([6])
        self.assertEqual(str(result.numerator), str(num))  # 5 (числитель)
        self.assertEqual(str(result.denominator), str(den))  # 6 (знаменатель), т.к. 1/2 + 1/3 = 5/6

    def test_add_negative_rationals(self):
        # Тест сложения отрицательных дробей
        r1 = Rational(Integer(Natural([1]), False), Natural([2]))  # -1/2
        r2 = Rational(Integer(Natural([1]), False), Natural([3]))  # -1/3
        result = self.add_qq_q.execute([r1, r2])[0]
        num = Integer(Natural([5]), False)
        den = Natural([6])
        self.assertEqual(str(result.numerator), str(num))  # -5 (числитель)
        self.assertEqual(str(result.denominator), str(den))  # 6 (знаменатель), т.к. -1/2 + -1/3 = -5/6

    def test_add_mixed_rationals(self):
        # Тест сложения смешанных дробей
        r1 = Rational(Integer(Natural([1]), True), Natural([2]))  # 1/2
        r2 = Rational(Integer(Natural([2]), True), Natural([3]))  # 2/3
        result = self.add_qq_q.execute([r1, r2])[0]
        num = Integer(Natural([7]), True)
        den = Natural([6])
        self.assertEqual(str(result.numerator), str(num))  # 7 (числитель)
        self.assertEqual(str(result.denominator), str(den))  # 6 (знаменатель), т.к. 1/2 + 2/3 = 7/6

    def test_add_zero_rational(self):
        # Тест сложения дроби с нулем
        r1 = Rational(Integer(Natural([1]), True), Natural([2]))  # 1/2
        r2 = Rational(Integer(Natural([0]), True), Natural([1]))  # 0/1 (ноль)
        result = self.add_qq_q.execute([r1, r2])[0]
        num = Integer(Natural([1]), True)
        den = Natural([2])
        self.assertEqual(str(result.numerator), str(num))  # 1 (числитель)
        self.assertEqual(str(result.denominator), str(den))  # 2 (знаменатель)

if __name__ == '__main__':
    unittest.main()
