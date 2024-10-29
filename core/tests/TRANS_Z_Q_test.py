import unittest
from data_types import *
from core.TRANS_Z_Q import TRANS_Z_Q


class TRANS_Z_Q_test(unittest.TestCase):
    def test_valid_integer(self):
        module = TRANS_Z_Q()
        #проверка для положительного целого числа
        integer = Integer(Natural([1, 2, 3]), is_positive=True)
        rational = Rational(integer, Natural([1]))
        result = module.execute([integer])
        self.assertEqual(result.numerator.natural.numbers, rational.numerator.natural.numbers)  # Проверяем, что совпадают знамянатели дробей

    def test_invalid_type(self):
        module = TRANS_Z_Q()
        with self.assertRaises(ValueError):
            module.execute([Rational(Integer(Natural([2])), Natural([1]))])
  
    def test_deepcopy(self):
        module = TRANS_Z_Q()
        integer = Integer(Natural([1, 2, 3]), is_positive=True) # создаем обьект класса Integer
        rational = Rational(integer, Natural([1]))
        result = module.execute([integer])  # Получаем массив с глубокой копией
        result.numerator.natural.numbers.append(4)  # Изменяем результат, добавляя новое значение

        # Проверяем, что измененный результат не равен оригинальному natural
        self.assertNotEqual(result.numerator.natural.numbers, rational.numerator.natural.numbers)  # Проверяем, что numbers в result изменились
        self.assertEqual( rational.numerator.natural.numbers, [1, 2, 3])  # Проверяем, что natural остался прежним


if __name__ == '__main__':
    unittest.main()