import unittest
from data_types import Natural, Integer, Rational, Polynomial
from core import DEG_P_N  # Импортируем класс, который тестируем

class TestDEG_P_N(unittest.TestCase):
    def setUp(self):
        self.degree_finder = DEG_P_N()

    def test_normal_polynomial(self):
        # Тест для многочлена 2x^3 + 0x^2 + 3x + 1 (степень должна быть 3)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([0])), Natural([1])),  # 0x^2
            Rational(Integer(Natural([2])), Natural([1]))   # 2x^3
        ])
        result = self.degree_finder.execute([poly])
        self.assertEqual(result, [3], "Степень многочлена должна быть 3")

    def test_polynomial_with_trailing_zeros(self):
        # Тест для многочлена 2x^3 + 3x + 1 + 0x^4 (последний нулевой коэффициент незначащий)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([0])), Natural([1])),  # 0x^2
            Rational(Integer(Natural([2])), Natural([1])),  # 2x^3
            Rational(Integer(Natural([0])), Natural([1]))   # 0x^4 (незначащий)
        ])
        result = self.degree_finder.execute([poly])
        self.assertEqual(result, [3], "Степень многочлена должна быть 3 (с учётом незначащих нулей)")

    def test_zero_polynomial(self):
        # Тест для многочлена, где все коэффициенты равны нулю
        poly = Polynomial([
            Rational(Integer(Natural([0])), Natural([1])),  # 0
        ])
        result = self.degree_finder.execute([poly])
        self.assertEqual(result, [0], "Степень нулевого многочлена должна быть 0")

    def test_invalid_argument(self):
        # Тест, если аргумент не является экземпляром Polynomial
        with self.assertRaises(ValueError):
            self.degree_finder.execute([42])  # Передан не Polynomial объект

if __name__ == "__main__":
    unittest.main()
