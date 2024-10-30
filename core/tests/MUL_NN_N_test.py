import unittest
from data_types import *
from core.MUL_NN_N import MUL_NN_N


class MUL_NN_N_test(unittest.TestCase):
    def setUp(self):
        self.mul_module = MUL_NN_N()

    def test_multiplication(self):
        # Умножение 12 * 34 = 408
        multiplier = Natural([2, 1])  # 12
        multiplicand = Natural([4, 3])  # 34
        result = self.mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.numbers, [8, 0, 4])


    def test_zero_multiplication(self):
        # Умножение 0 * 843 = 0
        multiplier = Natural([0])  # 0
        multiplicand = Natural([3, 4, 8])  # 843
        result = self.mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.numbers, [0])

    def test_multiplication_resulting_zero(self):
        # Умножение 12 * 0 = 0
        multiplier = Natural([2, 1])  # 21
        multiplicand = Natural([0])  # 0
        result = self.mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.numbers, [0])

    def test_one_multiplication(self):
        # Умножение 1456 * 1 = 1456
        multiplier = Natural([6, 5, 4, 1])  # 1456
        multiplicand = Natural([1])  # 1
        result = self.mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.numbers, [6, 5, 4, 1])

    def test_million_multiplication(self):
        # Умножение 234 * 1.000.000 = 234.000.000
        multiplier = Natural([4, 3, 2])  # 234
        multiplicand = Natural([0, 0, 0, 0, 0, 0, 1])  # 1.000.000
        result = self.mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.numbers, [0, 0, 0, 0, 0, 0, 4, 3, 2])

    def test_invalid_argument_count(self):
        # Проверка на неправильное число аргументов
        multiplier = Natural([2, 1])
        with self.assertRaises(ValueError):
            self.mul_module.execute([multiplier])  # Передаем только один аргумент

    def test_invalid_argument_type(self):
        # Проверка на неправильный тип аргумента
        multiplier = Natural([2, 1])
        invalid_argument = 4  # Неверный тип аргумента
        with self.assertRaises(ValueError):
            self.mul_module.execute([multiplier, invalid_argument])


if __name__ == "__main__":
    unittest.main()
