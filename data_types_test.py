import unittest
from data_types import Natural, Integer, Rational, Polynomial

class DataTypeTests(unittest.TestCase):
    def test_natural_simplify(self):
        n = Natural([1, 2])  # 21
        n.numbers.append(0)
        n.simplify()
        self.assertEqual(n.numbers, [1, 2])  # Проверяем, что нули убрались

    def test_integer_simplify(self):
        i = Integer(Natural([3]), is_positive=True)  # +30
        i.natural.numbers.append(0)
        i.natural.numbers.append(0)
        i.simplify()
        self.assertEqual(i.natural.numbers, [3])  # Проверяем, что нули убрались

    def test_rational_simplify(self):
        numerator = Integer(Natural([4]), is_positive=False)
        denominator = Natural([8])
        denominator.numbers.append(0)
        r = Rational(numerator, denominator)
        r.simplify()
        self.assertEqual(str(r), "-4/8")   # Проверяем, что нули убрались

    def test_polynomial_simplify(self):
        coeff1 = Rational(Integer(Natural([3])), Natural([1]))
        coeff2 = Rational(Integer(Natural([2])), Natural([1]))
        poly = Polynomial([coeff1, coeff2])
        poly.coefficients[0].numerator.natural.numbers.append(0)
        poly.simplify()
        self.assertEqual(str(poly), "3x + 2")   # Проверяем, что нули убрались


if __name__ == '__main__':
    unittest.main()
