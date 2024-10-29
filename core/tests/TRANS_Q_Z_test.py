import unittest
from data_types import *
from TRANS_Q_Z import TRANS_Q_Z


class TRANS_Q_Z_test(unittest.TestCase):
    def test_valid(self):
        module = TRANS_Q_Z()
        #проверка для положительного целого числа
        integer = Integer(Natural([1,2,3]), is_positive = True)
        rational = Rational(integer, Natural([1]))
        result = module.execute([rational])
        self.assertEqual(result.natural.numbers, integer.natural.numbers)  # Проверяем, что совпадают знамянатели дробей

    def test_invalid_type(self):
        module = TRANS_Q_Z()
        with self.assertRaises(ValueError):
            module.execute([Integer(Natural([2])), Natural([1])]) #проверка на выброс ошибки при передаче не правильного типа данных
   
    def test_deepcopy(self):
        module = TRANS_Q_Z()
        integer = Integer(Natural([1, 2, 3]), is_positive=True) # создаем обьект класса Integer
        rational = Rational(integer, Natural([1]))
        result = module.execute([rational])  # Получаем массив с глубокой копией
        result.natural.numbers.append(4)  # Изменяем результат, добавляя новое значение

        # Проверяем, что измененный результат не равен оригинальному natural
        self.assertNotEqual(result.natural.numbers, rational.numerator.natural.numbers)  # Проверяем, что numbers в result изменились
        self.assertEqual( rational.numerator.natural.numbers, [1, 2, 3])  # Проверяем, что natural остался прежним



if __name__ == '__main__':
    unittest.main()