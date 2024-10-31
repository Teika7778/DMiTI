import unittest
from core import LEAD_P_Q  # Импортируем наш класс LEAD_P_Q
from data_types import Natural, Integer, Rational, Polynomial  # Импорт необходимых классов

class TestLEAD_P_Q(unittest.TestCase):
    def setUp(self):
        self.lead_coeff_finder = LEAD_P_Q()

    def test_normal_polynomial(self):
        # Тест для многочлена 5x^3 + 0x^2 + 3x + 1 (старший коэффициент должен быть 5)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([0])), Natural([1])),  # 0x^2
            Rational(Integer(Natural([5])), Natural([1]))   # 5x^3 - старший коэффициент
        ])
        result = self.lead_coeff_finder.execute([poly])
        expected = [Rational(Integer(Natural([5])), Natural([1]))]
        self.assertEqual(result, expected, "Expected leading coefficient to be 5")

    def test_polynomial_with_trailing_zeros(self):
        # Тест для многочлена 5x^3 + 3x + 1 + 0x^4 (последний нулевой коэффициент незначащий)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([0])), Natural([1])),  # 0x^2
            Rational(Integer(Natural([5])), Natural([1])),  # 5x^3 - старший коэффициент
            Rational(Integer(Natural([0])), Natural([1]))   # 0x^4 (незначащий)
        ])
        result = self.lead_coeff_finder.execute([poly])
        expected = [Rational(Integer(Natural([5])), Natural([1]))]
        self.assertEqual(result, expected, "Expected leading coefficient to be 5, ignoring trailing zeros")

    def test_zero_polynomial(self):
        # Тест для многочлена, где все коэффициенты равны нулю (должен возвращать 0)
        poly = Polynomial([
            Rational(Integer(Natural([0])), Natural([1]))  # 0
        ])
        result = self.lead_coeff_finder.execute([poly])
        expected = [Rational(Integer(Natural([0])), Natural([1]))]
        self.assertEqual(result, expected, "Expected leading coefficient to be 0 for zero polynomial")

    def test_invalid_argument(self):
        # Тест, если аргумент не является экземпляром Polynomial
        with self.assertRaises(ValueError):
            self.lead_coeff_finder.execute([42])  # Передан не Polynomial объект

if __name__ == "__main__":
    unittest.main()
