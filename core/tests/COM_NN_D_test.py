import unittest  
from core import COM_NN_D as cnd
from data_types import Natural  

class COM_NN_D_test(unittest.TestCase):
    def setUp(self):  
        self.module = cnd.COM_NN_D()

    def test_first_number_is_greater(self):  
        n1 = Natural([3, 0, 5])  # 503  
        n2 = Natural([2, 9, 9])   # 992  
        self.assertEqual(self.module.execute([n1, n2]), [1])  # 503 < 992

    def test_second_number_is_greater(self):  
        n1 = Natural([6, 0, 1])   # 106  
        n2 = Natural([5, 0, 1])  # 105  
        self.assertEqual(self.module.execute([n1, n2]), [2])  # 106 > 105

    def test_numbers_are_equal(self):  
        n1 = Natural([1, 0, 1])  # 101  
        n2 = Natural([1, 0, 1])   # 101  
        self.assertEqual(self.module.execute([n1, n2]), [0])  # 101 == 101  

    def test_different_lengths_first_greater(self):  
        n1 = Natural([0, 1])      # 10  
        n2 = Natural([9])         # 9  
        self.assertEqual(self.module.execute([n1, n2]), [2])  # 10 > 9  

    def test_different_lengths_second_greater(self):  
        n1 = Natural([0, 1])      # 10  
        n2 = Natural([0, 0, 1])   # 100  
        self.assertEqual(self.module.execute([n1, n2]), [1])  # 10 < 100  

    def test_empty_numbers(self):  
        n1 = Natural([])          # 0  
        n2 = Natural([])          # 0  
        self.assertEqual(self.module.execute([n1, n2]), [0])  # 0 == 0  

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