import unittest
from core.GCF_NN_N import GCF_NN_N
from data_types import Natural


class GCF_NN_N_test(unittest.TestCase):
    def setUp(self):
        self.modul = GCF_NN_N()

    def test_gcf_zero(self):
        # НОД(0, 31) = 31
        n1 = Natural([0])  # 0
        n2 = Natural([1, 3]) # 31
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [1, 3])

    def test_gcf_second_zero(self):
        # НОД(254, 0) = 254
        n1 = Natural([4, 5, 2])  # 254
        n2 = Natural([0]) # 0
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [4, 5, 2])

    def test_gcf_one(self):
        # НОД(1, 14) = 1
        n1 = Natural([4, 1])  # 14
        n2 = Natural([1]) # 1
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [1])

    def test_gcf_first(self):
        # НОД(150, 4500) = 150
        n1 = Natural([0, 5, 1])  # 150
        n2 = Natural([0, 0, 5, 4]) # 4500
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [0, 5, 1])

    def test_gcf_equal(self):
        # НОД(123, 123) = 123
        n1 = Natural([3, 2, 1])  # 123
        n2 = Natural([3, 2, 1])  # 123
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [3, 2, 1])

    def test_gcf_prime_numbers(self):
        # НОД(13, 17) = 1
        n1 = Natural([3, 1])  # 13
        n2 = Natural([7, 1])  # 17
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [1])

    def test_gcf_large_numbers(self):
        # НОД(123456789, 987654321) = 9
        n1 = Natural([9, 8, 7, 6, 5, 4, 3, 2, 1])  # 123456789
        n2 = Natural([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 987654321
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [9])

    def test_gcf_any_numbers(self):
        # НОД(48, 18) = 6
        n1 = Natural([8, 4])  # 48
        n2 = Natural([8, 1])  # 18
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [6])

if __name__ == '__main__':
    unittest.main()
