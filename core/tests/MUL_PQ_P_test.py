import unittest
from data_types import *
from core.MUL_PQ_P import MUL_PQ_P  # Импортируем наш класс MUL_PQ_P


class TestMUL_PQ_P(unittest.TestCase):
    def setUp(self):
        self.mul_module = MUL_PQ_P()

    def test_multiply_polynomial_by_positive_rational(self):
        # Тест для умножения многочлена 3x^2 + 2x + 1 на 2/3
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([2])), Natural([1])),  # 2x
            Rational(Integer(Natural([3])), Natural([1]))  # 3x^2
        ])
        rational = Rational(Integer(Natural([2])), Natural([3]))  # 2/3
        result = self.mul_module.execute([poly, rational])

        expected_poly = Polynomial([
            Rational(Integer(Natural([2])), Natural([3])),  # 2/3
            Rational(Integer(Natural([4])), Natural([3])),  # 4/3 x
            Rational(Integer(Natural([6])), Natural([3]))  # 6/3 x^2
        ])

        # Сравнение строкового представления результата и ожидаемого значения
        self.assertEqual([str(coef) for coef in result[0].coefficients],
                         [str(coef) for coef in expected_poly.coefficients])

    def test_multiply_polynomial_by_zero_rational(self):
        # Тест для умножения многочлена на 0/1 (результат должен быть 0)
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([3])), Natural([1])),  # 3x
            Rational(Integer(Natural([5])), Natural([1]))  # 5x^2
        ])
        zero_rational = Rational(Integer(Natural([0])), Natural([1]))  # 0/1
        result = self.mul_module.execute([poly, zero_rational])

        expected_poly = Polynomial([Rational(Integer(Natural([0])), Natural([1]))])  # 0

        self.assertEqual([str(coef) for coef in result[0].coefficients],
                         [str(coef) for coef in expected_poly.coefficients])

    def test_multiply_polynomial_by_negative_rational(self):
        # Тест для умножения многочлена на отрицательное рациональное число -3/2
        poly = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),  # 1
            Rational(Integer(Natural([2])), Natural([1]))  # 2x
        ])
        negative_rational = Rational(Integer(Natural([3]), False), Natural([2]))  # -3/2
        result = self.mul_module.execute([poly, negative_rational])

        expected_poly = Polynomial([
            Rational(Integer(Natural([3]), False), Natural([2])),  # -3/2
            Rational(Integer(Natural([6]), False), Natural([2]))  # -6/2 x
        ])

        self.assertEqual([str(coef) for coef in result[0].coefficients],
                         [str(coef) for coef in expected_poly.coefficients])

    def test_invalid_argument_count(self):
        # Проверка на неправильное количество аргументов
        poly = Polynomial([Rational(Integer(Natural([1])), Natural([1]))])
        with self.assertRaises(ValueError):
            self.mul_module.execute([poly])  # Один аргумент

    def test_invalid_argument_type(self):
        # Проверка на неправильный тип аргументов
        poly = Polynomial([Rational(Integer(Natural([1])), Natural([1]))])
        invalid_rational = "Not ARGUME"
        with self.assertRaises(ValueError):
            self.mul_module.execute([poly, invalid_rational])  # Второй аргумент неправильного типа


if __name__ == "__main__":
    unittest.main()
