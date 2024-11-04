import unittest
from data_types import Natural, Integer, Rational, Polynomial

class DataTypeTests(unittest.TestCase):
    def test_zero_simplify(self):
        n = Natural([0])
        n.numbers.append(0)
        n.numbers.append(0)
        n.simplify()
        self.assertEqual(n.numbers, [0])
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

    def test_polynomial_simplify1(self):
        coeff1 = Rational(Integer(Natural([3])), Natural([1]))
        coeff2 = Rational(Integer(Natural([2])), Natural([1]))
        poly = Polynomial([coeff1, coeff2])
        poly.coefficients[0].numerator.natural.numbers.append(0)
        poly.simplify()
        self.assertEqual(str(poly), "3 + 2x")   # Проверяем, что нули убрались

    def test_polynomial_simplify2(self):
        coeff1 = Rational(Integer(Natural([0])), Natural([2]))
        coeff2 = Rational(Integer(Natural([2])), Natural([1]))
        poly = Polynomial([coeff1, coeff2])
        poly.coefficients[0].numerator.natural.numbers.append(0)
        poly.simplify()
        self.assertEqual(str(poly), "2x")  # Проверяем, что нули убрались
        self.assertEqual(len(poly.coefficients) - 1, 1)

    def test_polynomial_simplify2r(self):
        coeff2 = Rational(Integer(Natural([2])), Natural([1]))
        coeff1 = Rational(Integer(Natural([0])), Natural([2]))
        poly = Polynomial([coeff2, coeff1])
        poly.coefficients[0].numerator.natural.numbers.append(0)
        poly.simplify()
        self.assertEqual(str(poly), "2")  # Проверяем, что нули убрались
        self.assertEqual(len(poly.coefficients) - 1, 0)

    def test_polynomial_simplify3(self):
        coeff1 = Rational(Integer(Natural([1, 5, 3]), is_positive=False), Natural([2, 3]))
        coeff2 = Rational(Integer(Natural([1, 4, 3]), is_positive=False), Natural([2, 2]))
        coeff3 = Rational(Integer(Natural([1, 5, 3]), is_positive=True), Natural([2, 1]))
        poly = Polynomial([coeff1, coeff2, coeff3])
        poly.coefficients[0].numerator.natural.numbers.append(0)
        poly.simplify()
        self.assertEqual(str(poly), "-351/32 - 341/22x + 351/12x^2")  # Проверяем, что нули убрались

if __name__ == '__main__':
    unittest.main()
