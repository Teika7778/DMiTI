import unittest  
from core.COM_NN_D import COM_NN_D
from data_types import *

class COM_NN_D_test(unittest.TestCase):
    def setUp(self):  
        self.module = COM_NN_D()

    def test_first_number_is_greater(self):  
        n1 = Natural([3, 0, 5])  # 503  
        n2 = Natural([2, 9, 9])   # 992
        n3 = [Natural([1])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 503 < 992

    def test_second_number_is_greater(self):  
        n1 = Natural([6, 0, 1])   # 106  
        n2 = Natural([5, 0, 1])  # 105
        n3 = [Natural([2])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 106 > 105

    def test_numbers_are_equal(self):  
        n1 = Natural([1, 0, 1])  # 101  
        n2 = Natural([1, 0, 1])   # 101
        n3 = [Natural([0])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 101 == 101

    def test_different_lengths_first_greater(self):  
        n1 = Natural([0, 1])      # 10  
        n2 = Natural([9])         # 9
        n3 = [Natural([2])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 10 > 9

    def test_different_lengths_second_greater(self):  
        n1 = Natural([0, 1])      # 10  
        n2 = Natural([0, 0, 1])   # 100
        n3 = [Natural([1])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 10 < 100

    def test_empty_numbers(self):  
        n1 = Natural([])          # 0  
        n2 = Natural([])          # 0
        n3 = [Natural([0])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 0 == 0

    def test_invalid_arguments_length(self):  
        n1 = Natural([1])  
        with self.assertRaises(ValueError) as context:  
            self.module.execute([n1])  # Не хватает аргументов для сравнения  
        self.assertEqual(str(context.exception), "Необходимы два массива для сравнения.")  

    def test_invalid_arguments_type(self):  
        n1 = Natural([1])  
        with self.assertRaises(ValueError):  
            self.module.execute([n1, "string"])  # Неверный тип второго аргумента  

if __name__ == '__main__':  
    unittest.main()