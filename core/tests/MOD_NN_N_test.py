import unittest
from data_types import *
from core.MOD_NN_N import MOD_NN_N

class MOD_NN_N_test(unittest.TestCase):
    def test_invalid_args(self):  # проверка выброса исключений, если:
        module = MOD_NN_N()
        # список аргументов не list
        args1 = (Natural([1, 2, 3]), Natural([5, 6]))
        self.assertRaises(ValueError, module.execute, args1)

        # аргументов не ровно 2
        args2 = [Natural([1, 2, 3])]
        self.assertRaises(ValueError, module.execute, args2)

        # первый не Natural
        args3 = [(1, 2, 3), Natural([7])]
        self.assertRaises(ValueError, module.execute, args3)

        # второй не Natural
        args4 = [Natural([1, 4, 5]), Integer(Natural([5]))]
        self.assertRaises(ValueError, module.execute, args4)

    def test_valid_args(self):
        module = MOD_NN_N()
        #  общие случаи
        args1 = [Natural([7, 3, 2]), Natural([8, 1])]
        res1 = module.execute(args1)[0]
        self.assertEqual(res1.numbers, Natural([3]).numbers)

        args2 = [Natural([7, 7]), Natural([1, 1])]
        res2 = module.execute(args2)[0]
        self.assertEqual(res2.numbers, Natural([0]).numbers)

        args3 = [Natural([1, 1, 1]), Natural([9, 3])]
        res3 = module.execute(args3)[0]
        self.assertEqual(res3.numbers, Natural([3, 3]).numbers)

        # делимое меньше делителя
        args4 = [Natural([3, 3]), Natural([0, 0, 1])]
        res4 = module.execute(args4)[0]
        self.assertEqual(res4.numbers, Natural([3, 3]).numbers)

        args5 = [Natural([0]), Natural([0, 0, 1])]
        res5 = module.execute(args5)[0]
        self.assertEqual(res5.numbers, Natural([0]).numbers)

        # проверка выброса исключения при делении на 0
        args6 = [Natural([1, 8]), Natural([0])]
        self.assertRaises(ValueError, module.execute, args6)

if __name__ == '__main__':
    unittest.main()