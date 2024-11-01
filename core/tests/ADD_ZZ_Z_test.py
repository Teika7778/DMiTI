import unittest
from data_types import *
from core.ADD_ZZ_Z import ADD_ZZ_Z


class TestADD_ZZ_Z(unittest.TestCase):
    def test_add_positive_numbers(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([3, 4, 5]), is_positive=True)  # Число 543
        num2 = Integer(Natural([6, 7, 8]), is_positive=True)  # Число 876
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: 543 + 876 = 1419
        expected_result = Integer(Natural([9, 1, 4, 1]), is_positive=True)
        self.assertEqual(result.natural.numbers, expected_result.natural.numbers)
        self.assertEqual(result.is_positive, expected_result.is_positive)

    def test_add_negative_numbers(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([3, 4, 5]), is_positive=False)  # Число -543
        num2 = Integer(Natural([6, 7, 8]), is_positive=False)  # Число -876
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: -543 + (-876) = -1419
        expected_result = Integer(Natural([9, 1, 4, 1]), is_positive=False)
        self.assertEqual(result.natural.numbers, expected_result.natural.numbers)
        self.assertEqual(result.is_positive, expected_result.is_positive)

    def test_add_positive_and_negative(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([5, 4, 3]), is_positive=True)   # Число 345
        num2 = Integer(Natural([5, 4, 3]), is_positive=False)  # Число -345
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: 345 + (-345) = 0
        expected_result = Integer(Natural([0]), is_positive=True)
        self.assertEqual(result.natural.numbers, expected_result.natural.numbers)
        self.assertEqual(result.is_positive, expected_result.is_positive)

    def test_add_positive_and_smaller_negative(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([5, 5, 3]), is_positive=True)  # Число 355
        num2 = Integer(Natural([5, 4, 3]), is_positive=False)  # Число -345
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: 355 + (-345) = 10
        expected_result = Integer(Natural([0, 1]), is_positive=True)
        self.assertEqual(result.natural.numbers, expected_result.natural.numbers)
        self.assertEqual(result.is_positive, expected_result.is_positive)

    def test_add_negative_and_smaller_positive(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([5, 5, 3]), is_positive=False)  # Число -355
        num2 = Integer(Natural([5, 4, 3]), is_positive=True)   # Число 345
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: -355 + 345 = -10
        expected_result = Integer(Natural([0, 1]), is_positive=False)
        self.assertEqual(result.natural.numbers, expected_result.natural.numbers)
        self.assertEqual(result.is_positive, expected_result.is_positive)

    def test_add_positive_with_zero(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([3, 4, 5]), is_positive=True)  # Число 543
        num2 = Integer(Natural([0]), is_positive=True)        # Число 0
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: 543 + 0 = 543
        expected_result = Integer(Natural([3, 4, 5]), is_positive=True)
        self.assertEqual(str(result), str(expected_result))

    def test_add_negative_with_zero(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([3, 4, 5]), is_positive=False)  # Число -543
        num2 = Integer(Natural([0]), is_positive=True)         # Число 0
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: -543 + 0 = -543
        expected_result = Integer(Natural([3, 4, 5]), is_positive=False)
        self.assertEqual(str(result), str(expected_result))

    def test_add_zero_with_positive(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([0]), is_positive=True)        # Число 0
        num2 = Integer(Natural([7, 6, 5]), is_positive=True)  # Число 567
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: 0 + 567 = 567
        expected_result = Integer(Natural([7, 6, 5]), is_positive=True)
        self.assertEqual(str(result), str(expected_result))

    def test_add_zero_with_negative(self):
        add_module = ADD_ZZ_Z()
        num1 = Integer(Natural([0]), is_positive=True)         # Число 0
        num2 = Integer(Natural([2, 5, 8]), is_positive=False)  # Число -852
        result = add_module.execute([num1, num2])[0]

        # Ожидаемое значение: 0 + (-852) = -852
        expected_result = Integer(Natural([2, 5, 8]), is_positive=False)
        self.assertEqual(str(result), str(expected_result))


if __name__ == '__main__':
    unittest.main()
