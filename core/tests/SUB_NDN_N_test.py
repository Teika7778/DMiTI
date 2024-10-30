import unittest
from data_types import *
from core.SUB_NDN_N import SUB_NDN_N

class SUB_NDN_N_test(unittest.TestCase):
    def test_invalid_args(self):  # проверка выброса исключений, если:
        module = SUB_NDN_N()
        # список аргументов не list
        args1 = (Natural([1, 2, 3]), Natural([4]), Natural([5, 6]))
        self.assertRaises(ValueError, module.execute, args1)

        # аргументов не ровно 3
        args2 = [Natural([1, 2, 3]), Natural([4])]
        self.assertRaises(ValueError, module.execute, args2)

        # первый не Natural
        args3 = [(1, 2, 3), Natural([7]), Natural([1, 4])]
        self.assertRaises(ValueError, module.execute, args3)

        # второй не Natural
        args4 = [Natural([1, 4, 5]), Integer(Natural([5])), Natural([3, 3])]
        self.assertRaises(ValueError, module.execute, args4)

        # второй Natural, но не является цифрой
        args5 = [Natural([3, 3, 6]), Natural([1, 3]), Natural([1, 1])]
        self.assertRaises(ValueError, module.execute, args5)

        # третий не является Natural
        args6 = [Natural([1, 2, 3]), Natural([4]), 17]
        self.assertRaises(ValueError, module.execute, args6)

    def test_valid_args(self):
        module = SUB_NDN_N()
        #  общие случаи
        args1 = [Natural([3, 2, 1]), Natural([3]), Natural([7, 3])]
        res1 = module.execute(args1)[0]
        self.assertEqual(res1.numbers, Natural([2, 1]).numbers)

        args2 = [Natural([1, 3, 3, 1]), Natural([9]), Natural([8, 0, 1])]
        res2 = module.execute(args2)[0]
        self.assertEqual(res2.numbers, Natural([9, 5, 3]).numbers)

        # цифра равна 0
        args3 = [Natural([3, 1]), Natural([0]), Natural([9, 9, 9])]
        res3 = module.execute(args3)[0]
        self.assertEqual(res3.numbers, Natural([3, 1]).numbers)

        # результат равен 0
        args4 = [Natural([1, 0, 0, 1]), Natural([7]), Natural([3, 4, 1])]
        res4 = module.execute(args4)[0]
        self.assertEqual(res4.numbers, Natural([0]).numbers)

        # проверка выброса исключения, если результат отрицательный
        args5 = [Natural([1, 4, 3]), Natural([1]), Natural([2, 4, 3])]
        self.assertRaises(ValueError, module.execute, args5)

    def test_deepcopy(self):  # проверка на глубокую копию
        module = SUB_NDN_N()
        n = Natural([1, 2, 1])
        args = [n, Natural([5]), Natural([1, 1])]
        result = module.execute(args)[0]
        self.assertNotEqual(n.numbers[1], result.numbers[1])

if __name__ == '__main__':
    unittest.main()