import unittest
from core.SUB_ZZ_Z import SUB_ZZ_Z
from data_types import *

class SUB_NN_N_test(unittest.TestCase):

    def setUp(self):
        self.module = SUB_ZZ_Z()

    def test_simple_subtraction(self):
        n1 = Integer(Natural([5, 4]), is_positive=True)  # 45
        n2 = Integer(Natural([3, 1]), is_positive=True)  # 13
        n3 = Integer(Natural([2, 3]), is_positive=True) # 32 
        self.assertEqual(self.module.execute([n1, n2])[0].natural.numbers, n3.natural.numbers)  # 32

    def test_subtraction_resulting_in_zero(self):
        n1 = Integer(Natural([3, 1]), is_positive=True)  # 13
        n2 = Integer(Natural([3, 1]), is_positive=True)  # 13
        n3 = Integer(Natural([0]), is_positive=True) # 0
        self.assertEqual(self.module.execute([n1, n2])[0].natural.numbers, n3.natural.numbers)  # 0

    def test_second_greater(self):
        n1 = Integer(Natural([0, 1]), is_positive=True)  # 10
        n2 = Integer(Natural([3, 4]), is_positive=True)  # 43
        n3 = Integer(Natural([3, 3]), is_positive=False) # 33
        self.assertEqual(self.module.execute([n1, n2])[0].natural.numbers, n3.natural.numbers)  
        self.assertEqual(self.module.execute([n1, n2])[0].is_positive, n3.is_positive)  
    
    def test_second_greater_first_is_negative(self):
        n1 = Integer(Natural([0, 1]), is_positive = False)  # 10
        n2 = Integer(Natural([3, 4]), is_positive = True)  # 43
        n3 = Integer(Natural([3, 5]), is_positive = False) # 53
        self.assertEqual(self.module.execute([n1, n2])[0].natural.numbers, n3.natural.numbers)  
        self.assertEqual(self.module.execute([n1, n2])[0].is_positive, n3.is_positive)  

    def test_zeros(self):
        n1 = Integer(Natural([0]), is_positive=True)  # 0
        n2 = Integer(Natural([0]), is_positive=True)  # 0
        n3 = Integer(Natural([0]), is_positive=True) # 0
        self.assertEqual(self.module.execute([n1, n2])[0].natural.numbers, n3.natural.numbers)  # 0
        self.assertEqual(self.module.execute([n1, n2])[0].is_positive, n3.is_positive)  # 0

    def test_large_numbers(self):
        n1 = Integer(Natural([0] * 100 + [1]), is_positive=True)  # 1000...000 (1 с 100 нулями)
        n2 = Integer(Natural([1]), is_positive=True)    # 1
        n3 = Integer(Natural([9] * 100), is_positive=True) # 0
        self.assertEqual(self.module.execute([n1, n2])[0].natural.numbers, n3.natural.numbers)  # 999...999 (100 девяток)

if __name__ == '__main__':
    unittest.main()

