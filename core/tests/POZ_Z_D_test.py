import unittest
from core import POZ_Z_D as pzd
from data_types import *

class COM_NN_D_test(unittest.TestCase):
    def setUp(self):
        self.module = pzd.POZ_Z_D()

    def test_number_is_positive(self):
        n1 = Natural([0, 1])
        n2 = Integer(n1)
        self.assertEqual(self.module.execute([n2])[0].numbers, [2])

    def test_number_is_negative(self):
        n1 = Natural([0, 1])
        n2 = Integer(n1, False)
        self.assertEqual(self.module.execute([n2])[0].numbers, [1])

    def test_numbers_is_zero(self):
        n1 = Natural([0])
        n2 = Integer(n1)
        self.assertEqual(self.module.execute([n2])[0].numbers, [0])

    def test_invalid_arguments_length(self):
        with self.assertRaises(ValueError) as context:
            self.module.execute([])
        self.assertEqual(str(context.exception), "Invalid number of arguments")

    def test_invalid_arguments_type(self):
        n1 = Natural([1])
        with self.assertRaises(ValueError) as context:
            self.module.execute([n1])  # Неверный тип аргумента
        self.assertEqual(str(context.exception), "The number isn`t integer")

if __name__ == '__main__':
    unittest.main()
