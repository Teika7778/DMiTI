import unittest
from data_types import *
from core.INT_Q_B import INT_Q_B 


class INT_Q_B_test(unittest.TestCase):
    def test_valid_integer(self):
        module = INT_Q_B() #проверка для сокращенного дробного, которое целое 
        integer = Integer(Natural([1, 2, 3]), is_positive=True)
        rational = Rational(integer, Natural([1]))# создаем знамянатель равный 1 
        result = module.execute([rational])
        self.assertEqual(result,[True])  # Проверяем, что возвращаемое значение = True

    def test_non_integer(self):
        module = INT_Q_B() #проверка для сокращенного дробного, которое не целое 
        integer = Integer(Natural([1, 2, 3]), is_positive=True)
        rational = Rational(integer, Natural([3])) # создаем знамянатель не равный 1 
        result = module.execute([rational])
        self.assertEqual(result,[False])  # Проверяем, что возвращаемое значение = False

    def test_invalid_type(self):
        module = INT_Q_B()
        with self.assertRaises(ValueError):
            module.execute([Integer(Natural([2])), Natural([1])]) #  подается не рациональное число


if __name__ == '__main__':
    unittest.main()