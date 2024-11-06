import unittest
from data_types import *
from core.ADD_PP_P import ADD_PP_P

class TestADD_PP_P(unittest.TestCase):

    def test_add_polynomials_same_degree(self):
        add_pp_p = ADD_PP_P()
        # Полиномы 2x + 3 и 5x + 7
        poly1 = Polynomial([Rational(Integer(Natural([3])), Natural([1])), Rational(Integer(Natural([2])), Natural([1]))])
        poly2 = Polynomial([Rational(Integer(Natural([7])), Natural([1])), Rational(Integer(Natural([5])), Natural([1]))])
        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: 7x + 10
        expected_result = Polynomial([Rational(Integer(Natural([0, 1])), Natural([1])), Rational(Integer(Natural([7])), Natural([1]))])
        self.assertEqual(str(result), str(expected_result))

    def test_add_polynomials_different_degree(self):
        add_pp_p = ADD_PP_P()
        # Полиномы 4x^2 + 2x + 1 и x + 3
        poly1 = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),
            Rational(Integer(Natural([2])), Natural([1])),
            Rational(Integer(Natural([4])), Natural([1]))
        ])
        poly2 = Polynomial([
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1]))
        ])
        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: 4x^2 + 3x + 4
        expected_result = Polynomial([
            Rational(Integer(Natural([4])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([4])), Natural([1]))
        ])
        self.assertEqual(str(result), str(expected_result))

    def test_add_polynomial_with_zero(self):
        add_pp_p = ADD_PP_P()
        # Полиномы 3x^2 + 5 и 0
        poly1 = Polynomial([
            Rational(Integer(Natural([5])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1]))
        ])
        poly2 = Polynomial([
            Rational(Integer(Natural([0])), Natural([1]))
        ])
        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: 3x^2 + 5
        expected_result = Polynomial([
            Rational(Integer(Natural([5])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1]))
        ])
        self.assertEqual(str(result), str(expected_result))

    def test_add_polynomials_with_negative_coefficients(self):
        add_pp_p = ADD_PP_P()
        # Полиномы -2x + 3 и 5x - 7, СПЕЦИАЛЬНО УКАЗАН ЗНАК
        poly1 = Polynomial([Rational(Integer(Natural([3]), is_positive=True), Natural([1])),
                            Rational(Integer(Natural([2]), is_positive=False), Natural([1]))])
        poly2 = Polynomial([Rational(Integer(Natural([7]), is_positive=False), Natural([1])),
                            Rational(Integer(Natural([5]), is_positive=True), Natural([1]))])

        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: -4 + 3x
        expected_result = Polynomial([
            Rational(Integer(Natural([4]), is_positive=False), Natural([1])),
            Rational(Integer(Natural([3]), is_positive=True), Natural([1]))
        ])
        self.assertEqual(str(result), str(expected_result))

    def test_add_zero_polynomial_to_polynomial(self):
        add_pp_p = ADD_PP_P()
        # Полиномы 0 и 3x^2 + 5x + 1
        poly1 = Polynomial([Rational(Integer(Natural([0])), Natural([1]))])
        poly2 = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),
            Rational(Integer(Natural([5])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1]))
        ])

        result = add_pp_p.execute([poly1, poly2])[0]

        expected_result = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),
            Rational(Integer(Natural([5])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1]))
        ])

        # Ожидаемый результат: 3x^2 + 5x + 1
        self.assertEqual(str(result), str(expected_result))

    def test_add_polynomials_with_trailing_zeros(self):
        add_pp_p = ADD_PP_P()
        # Полиномы x^2 + 0x + 1 и -x + 0
        poly1 = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1]))
        ])
        poly2 = Polynomial([
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([1]), is_positive=False), Natural([1]))
        ])

        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: x^2 - x + 1
        expected_result = Polynomial([
            Rational(Integer(Natural([1])), Natural([1])),
            Rational(Integer(Natural([1]), is_positive=False), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1]))
        ])
        self.assertEqual(str(result), str(expected_result))

    def test_add_large_polynomials(self):
        add_pp_p = ADD_PP_P()
        # Полиномы 4x^5 + 3x^4 + 2x^3 + x^2 и x^3 + 2x^2 + 3x + 4
        poly1 = Polynomial([
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1])),
            Rational(Integer(Natural([2])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([4])), Natural([1]))
        ])
        poly2 = Polynomial([
            Rational(Integer(Natural([4])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([2])), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1]))
        ])

        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: 4x^5 + 3x^4 + 3x^3 + 3x^2 + 3x + 4
        expected_result = Polynomial([
            Rational(Integer(Natural([4])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([3])), Natural([1])),
            Rational(Integer(Natural([4])), Natural([1]))
        ])
        self.assertEqual(str(result), str(expected_result))

    def test_add_polynomials_with_one_term(self):
        add_pp_p = ADD_PP_P()
        # Полиномы 2 и x^3
        poly1 = Polynomial([Rational(Integer(Natural([2])), Natural([1]))])
        poly2 = Polynomial([
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1]))
        ])

        result = add_pp_p.execute([poly1, poly2])[0]

        # Ожидаемый результат: x^3 + 2
        expected_result = Polynomial([
            Rational(Integer(Natural([2])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([0])), Natural([1])),
            Rational(Integer(Natural([1])), Natural([1]))
        ])
        self.assertEqual(str(result), str(expected_result))


if __name__ == '__main__':
    unittest.main()
