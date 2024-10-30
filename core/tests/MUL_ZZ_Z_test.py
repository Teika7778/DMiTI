import unittest
from data_types import *
from core.MUL_ZZ_Z import MUL_ZZ_Z


class TestMulZZ_Z(unittest.TestCase):

    def test_positive_multiplication(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Умножение 12 * 34 = 408
        multiplier = Integer(Natural([2, 1]), is_positive=True)  # 12
        multiplicand = Integer(Natural([4, 3]), is_positive=True)  # 34
        result = mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.natural.numbers, [8, 0, 4])
        self.assertTrue(result.is_positive)

    def test_minus_1_multiplication(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Умножение 12 * 34 = 408
        multiplier = Integer(Natural([1]), is_positive=False)  # 12
        multiplicand = Integer(Natural([4, 3]), is_positive=True)  # 34
        result = mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.natural.numbers, [4, 3])
        self.assertFalse(result.is_positive)

    def test_negative_multiplication(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Умножение -12 * 34 = -408
        multiplier = Integer(Natural([2, 1]), is_positive=False)  # -12
        multiplicand = Integer(Natural([4, 3]), is_positive=True)  # 34
        result = mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.natural.numbers, [8, 0, 4])
        self.assertEqual(result.is_positive, False)

    def test_zero_multiplication(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Умножение 0 * 34 = 0
        multiplier = Integer(Natural([0]), is_positive=True)  # 0
        multiplicand = Integer(Natural([4, 3]), is_positive=True)  # 34
        result = mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.natural.numbers, [0])

    def test_multiplication_resulting_zero(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Умножение 12 * 0 = 0
        multiplier = Integer(Natural([2, 1]), is_positive=True)  # 12
        multiplicand = Integer(Natural([0]), is_positive=True)  # 0
        result = mul_module.execute([multiplier, multiplicand])[0]
        self.assertEqual(result.natural.numbers, [0])

    def test_invalid_argument_count(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Проверка на неправильное число аргументов
        multiplier = Integer(Natural([2, 1]), is_positive=True)
        with self.assertRaises(ValueError):
            mul_module.execute([multiplier])  # Передаем только один аргумент

    def test_invalid_argument_type(self):
        mul_module = MUL_ZZ_Z()  # Создаем экземпляр модуля
        # Проверка на неправильный тип аргумента
        multiplier = Integer(Natural([2, 1]), is_positive=True)
        invalid_argument = Natural([4, 3])  # Неверный тип аргумента
        with self.assertRaises(ValueError):
            mul_module.execute([multiplier, invalid_argument])


if __name__ == "__main__":
    unittest.main()
