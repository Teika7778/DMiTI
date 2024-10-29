import unittest
from data_types import Natural
from core.NZER_N_B import NZER_N_B

class TestNZERNB(unittest.TestCase):

    def setUp(self):
        self.module = NZER_N_B()

    def test_valid_non_zero_number(self):
        self.assertTrue(self.module.execute([Natural([5])]) )  # Ожидаем True, так как 5 не равно 0

    def test_valid_zero_number(self):
        self.assertFalse(self.module.execute([Natural([0])]))  # Ожидаем False, так как число равно 0

    def test_invalid_argument_count(self):
        # Проверка на количество аргументов
        with self.assertRaises(ValueError):
            self.module.execute([])  # Ожидаем ошибку, передан пустой массив
        with self.assertRaises(ValueError):
            self.module.execute([Natural([1]), Natural([2])])  # Ожидаем ошибку, передано два массива

    def test_invalid_arg_type(self):
        # Проверка на неверный тип аргументов
        with self.assertRaises(ValueError):
            self.module.execute(["not a natural"])  # Ожидаем ошибку, передан неверный тип


if __name__ == '__main__':
    unittest.main()