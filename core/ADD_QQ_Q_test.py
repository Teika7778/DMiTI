import unittest
from data_types import Rational  # Убедитесь, что этот импорт правильный
from core.ADD_QQ_Q import ADD_QQ_Q  # Убедитесь, что путь к классу верный

class TestADDQQQ(unittest.TestCase):

    def setUp(self):
        self.add_qq_q = ADD_QQ_Q()  # Создаем экземпляр класса для тестов

    def test_add_simple_rationals(self):
        r1 = Rational(1, 2)  # 1/2
        r2 = Rational(1, 3)  # 1/3
        result = self.add_qq_q.execute([r1, r2])
        expected = Rational(5, 6)  # 1/2 + 1/3 = 5/6
        self.assertEqual(result[0], expected)

    def test_add_with_different_denominators(self):
        r1 = Rational(1, 4)  # 1/4
        r2 = Rational(1, 2)  # 1/2
        result = self.add_qq_q.execute([r1, r2])
        expected = Rational(3, 4)  # 1/4 + 1/2 = 3/4
        self.assertEqual(result[0], expected)

    def test_add_with_negative_rationals(self):
        r1 = Rational(-1, 2)  # -1/2
        r2 = Rational(1, 3)   # 1/3
        result = self.add_qq_q.execute([r1, r2])
        expected = Rational(-1, 6)  # -1/2 + 1/3 = -1/6
        self.assertEqual(result[0], expected)

    def test_add_zero(self):
        r1 = Rational(0, 1)   # 0
        r2 = Rational(1, 3)   # 1/3
        result = self.add_qq_q.execute([r1, r2])
        expected = Rational(1, 3)  # 0 + 1/3 = 1/3
        self.assertEqual(result[0], expected)

    def test_invalid_argument_count(self):
        r1 = Rational(1, 2)
        with self.assertRaises(ValueError) as context:
            self.add_qq_q.execute([r1])  # недостаточно аргументов
        self.assertEqual(str(context.exception), "Неправильное количество аргументов: функция принимает 2 аргумента")

    def test_invalid_argument_type(self):
        r1 = Rational(1, 2)
        with self.assertRaises(ValueError) as context:
            self.add_qq_q.execute([r1, "not a rational"])  # неверный тип
        self.assertEqual(str(context.exception), "Неправильный тип данных: аргументы должны быть рациональными числами")

if __name__ == '__main__':
    unittest.main()
