import unittest
from data_types import *
from ABS_Z_N import abs_z_n

class abs_z_n_test(unittest.TestCase):
    def test_valid_integer(self):
        natural = Natural([1, 2, 3])
        integer = Integer(natural, is_positive=True)
        result = abs_z_n(integer)
        self.assertEqual(result[0].numbers, natural.numbers) # Проверяем, что при создании значения в result[0] совпадают с natural

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            abs_z_n(Rational(Integer(Natural([2])), Natural([1])))

    def test_deepcopy(self):
        natural = Natural([1, 2, 3])  # Создаем объект Natural
        integer = Integer(natural, is_positive=True)
        result = abs_z_n(integer)  # Получаем массив с глубокой копией
        result[0].numbers.append(4)   # Изменяем результат, добавляя новое значение

        # Проверяем, что измененный результат не равен оригинальному natural
        self.assertNotEqual(result[0].numbers, natural.numbers)  # Проверяем, что numbers в result изменились
        self.assertEqual(natural.numbers, [1, 2, 3])  # Проверяем, что natural остался прежним

if __name__ == '__main__':
    unittest.main()
