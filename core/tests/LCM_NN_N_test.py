import unittest
from core.LCM_NN_N import LCM_NN_N
from data_types import Natural


class LCM_NN_N_test(unittest.TestCase):
    def setUp(self):
        self.modul = LCM_NN_N()

    def test_lcm_zero(self):
        # НОК(0, 31) = 0
        n1 = Natural([0])  # 0
        n2 = Natural([1, 3]) # 31
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [0])

    def test_lcm_second_zero(self):
        # НОК(254, 0) = 0
        n1 = Natural([4, 5, 2])  # 254
        n2 = Natural([0]) # 0
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [0])

    def test_lcm_one(self):
        # НОК(1, 14) = 14
        n1 = Natural([4, 1])  # 14
        n2 = Natural([1]) # 1
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [4, 1])

    def test_lcm_equal(self):
        # НОК(123, 123) = 123
        n1 = Natural([3, 2, 1])  # 123
        n2 = Natural([3, 2, 1])  # 123
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [3, 2, 1])

    def test_lcm_prime_numbers(self):
        # НОК(13, 17) = 221
        n1 = Natural([3, 1])  # 13
        n2 = Natural([7, 1])  # 17
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [1, 2, 2])

    def test_lcm_large_numbers(self):
        # НОК(123456789, 987654321) = 13548070123626141
        n1 = Natural([9, 8, 7, 6, 5, 4, 3, 2, 1])  # 123456789
        n2 = Natural([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 987654321
        result = self.modul.execute([n1, n2])[0]
        expect = [1, 4, 1, 6, 2, 3, 6, 2, 0, 7, 8, 4, 5, 3, 1]
        self.assertEqual(result.numbers, expect)

    def test_lcm_any_numbers(self):
        # НОК(48, 18) = 144
        n1 = Natural([8, 4])  # 48
        n2 = Natural([8, 1])  # 18
        result = self.modul.execute([n1, n2])[0]
        self.assertEqual(result.numbers, [4, 4, 1])


if __name__ == '__main__':
    unittest.main()
