import unittest
from core.ADD_PP_P import ADD_PP_P  # Импортируем модуль ADD_PP_P для тестирования
from data_types import Natural, Integer, Rational, Polynomial

class ADD_PP_P_test(unittest.TestCase):
    def setUp(self):
        self.add_poly_module = ADD_PP_P()  # Инициализация модуля сложения многочленов

    def test_add_same_degree_polynomials(self):
        # Сложение (3/4)x^2 + (1/2)x + 2/3 и (5/6)x^2 + (2/3)x + 1/4
        poly1 = Polynomial([
            Rational(Integer(Natural([3])), Natural([4])),  # 3/4 x^2
            Rational(Integer(Natural([1])), Natural([2])),  # 1/2 x
            Rational(Integer(Natural([2])), Natural([3]))   # 2/3
        ])
        poly2 = Polynomial([
            Rational(Integer(Natural([5])), Natural([6])),  # 5/6 x^2
            Rational(Integer(Natural([2])), Natural([3])),  # 2/3 x
            Rational(Integer(Natural([1])), Natural([4]))   # 1/4
        ])
        result = self.add_poly_module.execute([poly1, poly2])[0]
        # Ожидаемый результат: (19/12)x^2 + (7/6)x + 11/12
        expected_coeffs = [
            Rational(Integer(Natural([9, 1])), Natural([2, 1])),  # 19/12 x^2
            Rational(Integer(Natural([7])), Natural([6])),        # 7/6 x
            Rational(Integer(Natural([1, 1])), Natural([2, 1]))   # 11/12
        ]
        self.assertEqual(
            [str(result.coefficients[i]) for i in range(len(result.coefficients))],
            [str(expected_coeffs[i]) for i in range(len(expected_coeffs))]
        )

    def test_add_different_degree_polynomials(self):
        # Сложение (x^3 + 3/2) и (5x^2 + 1/3)
        poly1 = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),        # 1 x^3
            Rational(Integer(Natural([0])), Natural([1])),        # 0 x^2
            Rational(Integer(Natural([0])), Natural([1])),        # 0 x
            Rational(Integer(Natural([3])), Natural([2]))         # 3/2
        ])
        poly2 = Polynomial([
            Rational(Integer(Natural([5])), Natural([1])),        # 5 x^2
            Rational(Integer(Natural([0])), Natural([1])),        # 0 x
            Rational(Integer(Natural([1])), Natural([3]))         # 1/3
        ])
        result = self.add_poly_module.execute([poly1, poly2])[0]
        # Ожидаемый результат: x^3 + 5x^2 + 0x + 13/6
        expected_coeffs = [
            Rational(Integer(Natural([1])), Natural([1])),        # 1 x^3
            Rational(Integer(Natural([5])), Natural([1])),        # 5 x^2
            Rational(Integer(Natural([0])), Natural([1])),        # 0 x
            Rational(Integer(Natural([1, 3])), Natural([6]))      # 13/6
        ]
        self.assertEqual(
            [str(result.coefficients[i]) for i in range(len(result.coefficients))],
            [str(expected_coeffs[i]) for i in range(len(expected_coeffs))]
        )

    def test_zero_polynomial(self):
        # Сложение нулевого многочлена с другим многочленом
        poly1 = Polynomial([Rational(Integer(Natural([0])), Natural([1]))])  # 0
        poly2 = Polynomial([
            Rational(Integer(Natural([5])), Natural([4])),       # 5/4
            Rational(Integer(Natural([3])), Natural([2]))        # 3/2
        ])
        result = self.add_poly_module.execute([poly1, poly2])[0]
        # Ожидаемый результат: тот же второй полином
        self.assertEqual(
            [str(result.coefficients[i]) for i in range(len(result.coefficients))],
            [str(poly2.coefficients[i]) for i in range(len(poly2.coefficients))]
        )

    def test_invalid_argument_count(self):
        # Неправильное количество аргументов (ожидается ошибка)
        poly = Polynomial([Rational(Integer(Natural([1])), Natural([2]))])  # 1/2
        with self.assertRaises(ValueError):
            self.add_poly_module.execute([poly])  # Один аргумент вместо двух

    def test_invalid_argument_type(self):
        # Проверка, если тип аргумента неверный (ожидается ошибка)
        poly = Polynomial([Rational(Integer(Natural([1])), Natural([2]))])  # 1/2
        invalid_argument = "Invalid argument type"
        with self.assertRaises(ValueError):
            self.add_poly_module.execute([poly, invalid_argument])  # Второй аргумент не Polynomial

if __name__ == '__main__':
    unittest.main()
