import unittest
from core.MUL_ZM_Z import MUL_ZM_Z
from data_types import *

class MUL_ZM_Z_test(unittest.TestCase):
    def setUp(self):
        self.module = MUL_ZM_Z()

    def test_number_is_positive(self):
        n1 = Natural([0, 1, 2])
        n2 = Integer(n1)
        result = self.module.execute([n2])
        self.assertEqual(result[0].is_positive, False)

    def test_number_is_negative(self):
        n1 = Natural([5, 4, 1])
        n2 = Integer(n1, False)
        result = self.module.execute([n2])
        self.assertEqual(result[0].is_positive, True)

    def test_numbers_is_zero(self):
        n1 = Natural([0])
        n2 = Integer(n1)
        result = self.module.execute([n2])
        self.assertEqual(result[0].is_positive, True)

    def test_invalid_arguments_length(self):
        with self.assertRaises(ValueError) as context:
            self.module.execute([])  # неверное количество аргументов
        self.assertEqual(str(context.exception), "Invalid number of arguments")

    def test_invalid_arguments_type(self):
        n1 = Natural([1])
        with self.assertRaises(ValueError) as context:
            self.module.execute([n1])  # неверный тип аргумента
        self.assertEqual(str(context.exception), "The number isn`t integer")

if __name__ == '__main__':
    unittest.main()