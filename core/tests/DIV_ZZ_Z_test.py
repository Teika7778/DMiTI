import unittest
from core.DIV_ZZ_Z import DIV_ZZ_Z
from data_types import *


class DIV_ZZ_Z_test(unittest.TestCase):
    def setUp(self):
        self.module = DIV_ZZ_Z()

    def test_dividing_the_positive_by_the_positive_without_remainder(self):
        n1 = Integer(Natural([0, 1]), True)
        n2 = Integer(Natural([5]), True)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [2])  # 10 // 5 = 2
        self.assertEqual(result[0].is_positive, True)

    def test_dividing_the_negative_by_the_negative_without_remainder(self):
        n1 = Integer(Natural([6, 1]), False)
        n2 = Integer(Natural([4]), False)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [4])  # -16 // -4 = 4
        self.assertEqual(result[0].is_positive, True)

    def test_dividing_the_positive_by_the_negative_without_remainder(self):
        n1 = Integer(Natural([5, 3]), True)
        n2 = Integer(Natural([7]), False)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [5])  # 35 // -7 = -5
        self.assertEqual(result[0].is_positive, False)

    def test_dividing_the_negative_by_the_positive_without_remainder(self):
        n1 = Integer(Natural([2, 2]), False)
        n2 = Integer(Natural([1, 1]), True)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [2])  # -22 // 11 = -2
        self.assertEqual(result[0].is_positive, False)
    def test_dividing_the_positive_by_the_positive(self):
        n1 = Integer(Natural([1, 2]))
        n2 = Integer(Natural([5]))
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [4])  # 21 // 5 = 4(ост.1)
        self.assertEqual(result[0].is_positive, True)

    def test_dividing_the_negative_by_the_negative(self):
        n1 = Integer(Natural([1, 7]), False)
        n2 = Integer(Natural([0, 1]), False)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [8])  # -71 // -10 = 7(ост.-1) => -71 // -10 = 8(ост.9)
        self.assertEqual(result[0].is_positive, True)

    def test_dividing_the_positive_by_the_negative(self):
        n1 = Integer(Natural([5, 3]), True)
        n2 = Integer(Natural([8]), False)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [4])  # 35 // -8 = -4(ост.3)
        self.assertEqual(result[0].is_positive, False)

    def test_dividing_the_negative_by_the_positive(self):
        n1 = Integer(Natural([2, 2]), False)
        n2 = Integer(Natural([7, 1]), True)
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].natural.numbers, [2])  # -22 // 17 = -1(ост.-5) => -22 // 17 = -2(ост12)
        self.assertEqual(result[0].is_positive, False)

    def test_divisor_is_zero(self):
        n1 = Integer(Natural([5]))
        n2 = Integer(Natural([0]))
        with self.assertRaises(ValueError) as context:
            self.module.execute([n1, n2])  # деление на 0
        self.assertEqual(str(context.exception), "The divisor cannot be zero")

    def test_invalid_arguments_length(self):
        with self.assertRaises(ValueError) as context:
            self.module.execute([])  # неверное количество аргументов
        self.assertEqual(str(context.exception), "Invalid number of arguments")

    def test_invalid_arguments_type(self):
        n1 = Natural([1])
        n2 = Integer(n1)
        with self.assertRaises(ValueError) as context:
            self.module.execute([n1, n2])  # неверный тип аргумента
        self.assertEqual(str(context.exception), "The number isn`t integer")

if __name__ == '__main__':
    unittest.main()