import unittest
from data_types import *
from core.ABS_Z_N import ABS_Z_N


class ABS_Z_N_test(unittest.TestCase):
    def test_valid_integer(self):
        natural = Natural([1, 2, 3])
        integer = Integer(natural, is_positive=True)
        result = ABS_Z_N([integer])
        self.assertEqual(result[0].numbers,
                         natural.numbers)  # Проверяем, что при создании значения в result[0] совпадают с natural

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            ABS_Z_N([Rational(Integer(Natural([2])), Natural([1]))])

    def test_deepcopy(self):
        natural = Natural([1, 2, 3])  # Создаем объект Natural
        integer = Integer(natural, is_positive=True)
        result = ABS_Z_N([integer])  # Получаем массив с глубокой копией
        result[0].numbers.append(4)  # Изменяем результат, добавляя новое значение

        # Проверяем, что измененный результат не равен оригинальному natural
        self.assertNotEqual(result[0].numbers, natural.numbers)  # Проверяем, что numbers в result изменились
        self.assertEqual(natural.numbers, [1, 2, 3])  # Проверяем, что natural остался прежним


if __name__ == '__main__':
    unittest.main()
