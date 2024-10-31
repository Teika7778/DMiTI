import unittest
from core.MUL_PQ_P import MUL_PQ_P  # Импортируем класс
from data_types import Natural, Integer, Rational, Polynomial  # Импортируем необходимые типы

class TestMUL_PQ_P(unittest.TestCase):
    def setUp(self):
        self.multiplier = MUL_PQ_P()

    def test_multiply_by_positive_rational(self):
        # Тест для многочлена 1 + 3x + 5x^2 и умножение на 2 (2/1)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([5])), Natural([1]))   # 5x^2
        ])
        rational = Rational(Integer(Natural([2])), Natural([1]))  # Умножаем на 2

        result = self.multiplier.execute([poly, rational])
        expected = Polynomial([
            Rational(Integer(Natural([2])), Natural([1])),  # 2
            Rational(Integer(Natural([6])), Natural([1])),  # 6x
            Rational(Integer(Natural([10])), Natural([1]))  # 10x^2
        ])
        self.assertEqual(result[0].coefficients, expected.coefficients, "Expected each coefficient to be multiplied by 2")

    def test_multiply_by_zero(self):
        # Тест для многочлена 1 + 3x + 5x^2 и умножение на 0
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([5])), Natural([1]))   # 5x^2
        ])
        rational = Rational(Integer(Natural([0])), Natural([1]))  # Умножаем на 0

        result = self.multiplier.execute([poly, rational])
        expected = Polynomial([
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([0])), Natural([1])),  # 0
            Rational(Integer(Natural([0])), Natural([1]))   # 0
        ])
        self.assertEqual(result[0].coefficients, expected.coefficients, "Expected each coefficient to be 0 after multiplication")

    def test_multiply_by_negative_rational(self):
        # Тест для многочлена 1 + 3x + 5x^2 и умножение на -1 (т.е. -1/1)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([5])), Natural([1]))   # 5x^2
        ])
        rational = Rational(Integer(Natural([1]), is_positive=False), Natural([1]))  # Умножаем на -1

        result = self.multiplier.execute([poly, rational])
        expected = Polynomial([
            Rational(Integer(Natural([1]), is_positive=False), Natural([1])),  # -1
            Rational(Integer(Natural([3]), is_positive=False), Natural([1])),  # -3x
            Rational(Integer(Natural([5]), is_positive=False), Natural([1]))   # -5x^2
        ])
        self.assertEqual(result[0].coefficients, expected.coefficients, "Expected each coefficient to be multiplied by -1")

    def test_invalid_argument(self):
        # Тест для случая, когда аргумент не является Polynomial или Rational
        with self.assertRaises(ValueError):
            self.multiplier.execute([42, Rational(Integer(Natural([1])), Natural([1]))])  # Передан не Polynomial
        with self.assertRaises(ValueError):
            self.multiplier.execute([Polynomial([]), 42])  # Передан не Rational

if __name__ == "__main__":
    unittest.main()
