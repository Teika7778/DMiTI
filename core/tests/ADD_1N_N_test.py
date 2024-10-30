import unittest
from data_types import *
from core.ADD_1N_N import ADD_1N_N

class ADD_1N_N_test(unittest.TestCase):
    def test_invalid_args(self):
        module = ADD_1N_N()
        args1 = (Natural([1, 2, 3]),)
        self.assertRaises(ValueError, module.execute, args1)  # проверка,
        # выбрасывается ли исключение, если список аргументов не list

        args2 = [Natural([1, 2, 3]), Natural([3, 4, 5])]
        self.assertRaises(ValueError, module.execute, args2)  # проверка,
        # выбрасывается ли исключение, если аргументов не ровно 1

        args3 = [[1, 2, 3]]
        self.assertRaises(ValueError, module.execute, args3)  # проверка,
        # выбрасывается ли исключение, если аргумент не Natural

    def test_valid_args(self):  # проверки результата работы
        module = ADD_1N_N()
        # общие случаи
        n1 = module.execute([Natural([1, 2, 3])])[0]
        self.assertEqual(n1.numbers, Natural([2, 2, 3]).numbers)
        n2 = module.execute([Natural([3, 4, 5])])[0]
        self.assertEqual(n2.numbers, Natural([4, 4, 5]).numbers)
        # частный случай
        n3 = module.execute([Natural([9, 9, 1, 1])])[0]
        self.assertEqual(n3.numbers, Natural([0, 0, 2, 1]).numbers)
        # еще более частный
        n4 = module.execute([Natural([9, 9,])])[0]
        self.assertEqual(n4.numbers, Natural([0, 0, 1]).numbers)

    def test_deepcopy(self):  # проверка на глубокую копию
        module = ADD_1N_N()
        n = Natural([1, 2, 3])
        result = module.execute([n])
        result[0].numbers[0] = 4
        self.assertNotEqual(result[0].numbers[0], n.numbers[0])

if __name__ == '__main__':
    unittest.main()