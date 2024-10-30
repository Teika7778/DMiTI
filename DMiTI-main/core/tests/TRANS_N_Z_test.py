import unittest
from core.TRANS_N_Z import TRANS_N_Z
from data_types import *

class TRANS_N_Z_test(unittest.TestCase):
    def setUp(self):
        self.module = TRANS_N_Z()

    def test_trans_natural_in_integer(self):
        n1 = Natural([0, 1])
        result = self.module.execute([n1])
        self.assertEqual(type(result[0]), Integer)

    def test_invalid_arguments_length(self):
        with self.assertRaises(ValueError) as context:
            self.module.execute([])  # неверное количество аргументов
        self.assertEqual(str(context.exception), "Invalid number of arguments")

    def test_invalid_arguments_type(self):
        n1 = Natural([1])
        n2 = Integer(n1)

        with self.assertRaises(ValueError) as context:
            self.module.execute([n2])  # неверный тип аргумента
        self.assertEqual(str(context.exception), "The number isn`t natural")

if __name__ == '__main__':
    unittest.main()