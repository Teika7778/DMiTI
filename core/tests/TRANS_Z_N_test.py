import unittest
from core.TRANS_Z_N import TRANS_Z_N
from data_types import *

class TRANS_Z_N_test(unittest.TestCase):
    def setUp(self):
        self.module = TRANS_Z_N()

    def test_trans_natural_in_integer(self):
        n1 = Natural([0, 1])
        n2 = Integer(n1)
        result = self.module.execute([n2])
        self.assertEqual(type(result[0]), Natural)

    def test_invalid_sign(self):
        n1 = Natural([1, 1, 1])
        n2 = Integer(n1, False)
        with self.assertRaises(ValueError) as context:
            self.module.execute([n2])  # неверный тип знака
        self.assertEqual(str(context.exception), "The integer must be positive")

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