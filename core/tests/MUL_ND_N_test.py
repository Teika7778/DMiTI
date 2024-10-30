import unittest
from data_types import Natural
from core.MUL_ND_N import MUL_ND_N


class MUL_ND_N_test(unittest.TestCase):
    def setUp(self):
        self.module = MUL_ND_N()

    def test_multiply_by_zero(self):
        n1 = Natural([1, 2, 3])  # 321
        n2 = Natural([0])
        n3 = [Natural([0])]
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].numbers, n3[0].numbers)  # Ожидаем [0]

    def test_multiply_by_one(self):
        n1 = Natural([4, 5, 6])  # 654
        n2 = Natural([1])
        n3 = [Natural([4, 5, 6])]
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].numbers, n3[0].numbers)  # Ожидаем 654

    def test_multiply_by_two(self):
        n1 = Natural([1, 2, 7])  # 721
        n2 = Natural([2])
        n3 = [Natural([2, 4, 4, 1])]
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].numbers, n3[0].numbers)  # Ожидаем 1442

    def test_multiply_by_nine(self):
        n1 = Natural([9, 8, 7])  # 789
        n2 = Natural([9])
        n3 = [Natural([1, 0, 1, 7])]
        result = self.module.execute([n1, n2])
        self.assertEqual(result[0].numbers, n3[0].numbers) # Ожидаем 7101

    def test_invalid_natural(self):
        with self.assertRaises(ValueError):
            self.module.execute([None, Natural([2])])  # Первый аргумент не Natural

    def test_invalid_digit(self):
        n1 = Natural([1, 2])
        n2 = Natural([1, 2])
        with self.assertRaises(ValueError):
            self.module.execute([n1, n2])  # Второй аргумент не натуральное число с одной цифрой


if __name__ == '__main__':
    unittest.main()
