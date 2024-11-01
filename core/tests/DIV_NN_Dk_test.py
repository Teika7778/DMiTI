import unittest
from data_types import *
from core.DIV_NN_Dk import DIV_NN_Dk

class DIV_NN_Dk_test(unittest.TestCase):
    def test_invalid_args(self):  # проверка выброса исключений, если:
        module = DIV_NN_Dk()
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
        module = DIV_NN_Dk()
        #  общие случаи
        args1 = [Natural([3, 2, 2]), Natural([0, 0, 1])]
        res1 = module.execute(args1)[0]
        self.assertEqual(res1.numbers, Natural([2]).numbers)

        args2 = [Natural([9, 6, 6]), Natural([3, 1])]
        res2 = module.execute(args2)[0]
        self.assertEqual(res2.numbers, Natural([0, 5]).numbers)

        args3 = [Natural([7, 0, 0, 2]), Natural([9, 1])]
        res3 = module.execute(args3)[0]
        self.assertEqual(res3.numbers, Natural([0, 0, 1]).numbers)

        # делим на 1
        args4 = [Natural([1, 2, 3]), Natural([1])]
        res4 = module.execute(args4)[0]
        self.assertEqual(res4.numbers, Natural([0, 0, 3]).numbers)

        # деление на само себя
        args5 = [Natural([2, 3, 4]), Natural([2, 3, 4])]
        res5 = module.execute(args5)[0]
        self.assertEqual(res5.numbers, Natural([1]).numbers)

        # проверка выброса исключения, когда первое натуральное меньше второго
        args6 = [Natural([1, 4, 3]), Natural([2, 4, 3, 2])]
        self.assertRaises(ValueError, module.execute, args6)

        # проверка выброса исключения при делении на 0
        args7 = [Natural([1, 8]), Natural([0])]
        self.assertRaises(ValueError, module.execute, args7)

if __name__ == '__main__':
    unittest.main()