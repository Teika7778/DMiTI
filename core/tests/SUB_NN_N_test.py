import unittest
import unittest
from core.SUB_NN_N import SUB_NN_N
from data_types import Natural

class SUB_NN_N_test(unittest.TestCase):

    def setUp(self):
        self.module = SUB_NN_N()

    def test_simple_subtraction(self):
        n1 = Natural([5, 4])  # 45
        n2 = Natural([3, 1])  # 13
        n3 = [Natural([2,3])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 32

    def test_subtraction_resulting_in_zero(self):
        n1 = Natural([2])      # 2
        n2 = Natural([2])      # 2
        n3 = [Natural([0])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 0


    def test_invalid_subtraction(self):
        n1 = Natural([1])    # 1
        n2 = Natural([2])    # 2
        with self.assertRaises(ValueError) as context:
            self.module.execute([n1, n2])  # Первое меньше второго
        self.assertEqual(str(context.exception), "Первое число должно быть больше или равно.")

    def test_different_lengths(self):
        n1 = Natural([3, 2, 1])  # 123
        n2 = Natural([2, 1])      # 12
        n3 = [Natural([1,1,1])]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)

    def test_large_numbers(self):
        n1 = Natural([0] * 100 + [1])  # 1000...000 (1 с 100 нулями)
        n2 = Natural([1])                # 1
        n3 = [Natural([9] * 100)]
        self.assertEqual(self.module.execute([n1, n2])[0].numbers, n3[0].numbers)  # 999...999 (100 девяток)

if __name__ == '__main__':
    unittest.main()

