import unittest  
from core.ADD_NN_N import ADD_NN_N
from data_types import Natural  

class ADD_NN_N_test(unittest.TestCase):
    def setUp(self):  
        self.module = ADD_NN_N()

    def test_simple_addition(self):  
        n1 = Natural([3, 4])  # 43  
        n2 = Natural([2, 5])  # 52
        n3 = [Natural([5, 9])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 95

    def test_addition_with_carry(self):  
        n1 = Natural([9, 9])  # 99  
        n2 = Natural([1])     # 1  
        n3 = [Natural([0, 0, 1])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 100

    def test_adding_zero(self):  
        n1 = Natural([0])        # 0  
        n2 = Natural([4, 2])     # 24  
        n3 = [Natural([4, 2])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 42

    def test_adding_two_zeros(self):  
        n1 = Natural([0])        # 0  
        n2 = Natural([0])        # 0  
        n3 = [Natural([0])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 0

    def test_invalid_arguments_length(self):  
        n1 = Natural([1, 2])  
        with self.assertRaises(ValueError) as context:  
            self.module.execute([n1])  # Не хватает аргументов для сложения  
        self.assertEqual(str(context.exception), "Необходимы два массива для сравнения.")

    def test_invalid_arguments_type(self):  
        n1 = Natural([1])  
        with self.assertRaises(ValueError):  
            self.module.execute([n1, "string"])  # Неверный тип второго аргумента  

    def test_addition_with_different_lengths(self):  
        n1 = Natural([1, 2, 3])  # 321  
        n2 = Natural([9, 8])      # 89  
        n3 = [Natural([0, 1, 4])] #410
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 410

    def test_large_numbers(self):  
        n1 = Natural([9] * 100)  # 999...999 (100 девяток)  
        n2 = Natural([1]) # 1
        n3 = [Natural([0]*100 + [1])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers,n3[0].numbers)  # 100    # 1000...000 (1, с 100 нулями)

if __name__ == '__main__':  
    unittest.main()