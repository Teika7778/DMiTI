import unittest
from core import MUL_Nk_N as mulnk
from data_types import Natural


class MUL_Nk_N_TEST(unittest.TestCase):

    def setUp(self):
        self.module = mulnk.MUL_Nk_N()

    def test_multiplication_by_zero(self):
        n1 = Natural([0, 1])  # Натуральное N
        n2 = Natural([0])  # Натуральное k
        result = self.module.execute([n1, n2])  # Запись результата работы MUL_Nk_N
        expected = [Natural([0, 1])]  # Ожидаемый результат
        self.assertEqual(result[0].numbers, expected[0].numbers)  # Сравнение ожидаемого и фактического результатов

    def test_multiplication_by_one(self):
        n1 = Natural([2, 4, 1])  # Натуральное N
        n2 = Natural([1])  # Натуральное k
        result = self.module.execute([n1, n2])  # Запись результата работы MUL_Nk_N
        expected = [Natural([0, 2, 4, 1])]  # Ожидаемый результат
        self.assertEqual(result[0].numbers, expected[0].numbers)  # Сравнение ожидаемого и фактического результатов

    def test_multiplication_by_million(self):
        n1 = Natural([2, 4, 1])  # Натуральное N
        n2 = Natural([0, 0, 0, 0, 0, 0, 1])  # Натуральное k
        result = self.module.execute([n1, n2])  # Запись результата работы MUL_Nk_N
        expected = [Natural([0] * 1000000 + n1.numbers)]  # Ожидаемый результат
        self.assertEqual(result[0].numbers, expected[0].numbers)  # Сравнение ожидаемого и фактического результатов



if __name__ == '__main__':
    unittest.main()
