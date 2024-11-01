import unittest
from core.RED_Q_Q import RED_Q_Q
from data_types import *

class RED_Q_Q_test(unittest.TestCase):

    def setUp(self):
        self.module = RED_Q_Q()

    def test_simple_red(self):
        n1 = Natural([0, 2])  # 20
        n2 = Integer(Natural([0, 1]), is_positive = True)  # 10
        rational = Rational(n2,n1)
        result = self.module.execute([rational])[0]
        self.assertEqual(result.numerator.natural.numbers, Natural([1]).numbers) #1
        self.assertEqual(result.denominator.numbers, Natural([2]).numbers) #1


if __name__ == '__main__':
    unittest.main()

