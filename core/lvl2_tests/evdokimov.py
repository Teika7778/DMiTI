import unittest
from core.ADD_1N_N import ADD_1N_N
from core.ADD_NN_N import ADD_NN_N
from core.COM_NN_D import COM_NN_D
from core.DIV_NN_Dk import DIV_NN_Dk
from core.DIV_NN_N import DIV_NN_N
from core.LCM_NN_N import LCM_NN_N
from core.GCF_NN_N import GCF_NN_N
from core.MOD_NN_N import MOD_NN_N
from core.MUL_NN_N import MUL_NN_N
from core.SUB_NN_N import SUB_NN_N
from data_types import *


def getInt(n):
    return int("".join(list(map(str, n.numbers[::-1]))))


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.add_1n = ADD_1N_N()   # +
        self.add_nn = ADD_NN_N()   # +
        self.com_nn = COM_NN_D()   # +
        self.div_nn = DIV_NN_N()   #
        self.lcm_nn = LCM_NN_N()   #
        self.gcf_nn = GCF_NN_N()   #
        self.mod_nn = MOD_NN_N()   #
        self.mul_nn = MUL_NN_N()   #
        self.sub_nn = SUB_NN_N()   # +

        self.n1 = Natural([0]*100 + [1] * 100)
        self.n2 = Natural([9]*1000)
        self.n2_c = Natural([9]*1000)
        self.n3 = Natural([1]*100)
        self.zero = Natural([0])

    def testNaturalAndPoly(self):
        #СЛОЖЕНИЕ, ВЫЧИТАНИЕ, СРАВНЕНИЕ
        res1 = self.add_nn.execute([self.n2, self.n3])[0]
        self.assertEqual(getInt(res1), getInt(self.n2) + getInt(self.n3))
        res2 = self.add_nn.execute([res1, self.n1])[0]
        self.assertEqual(getInt(res2), getInt(res1) + getInt(self.n1))
        res3 = self.add_nn.execute([res2, self.zero])[0]
        self.assertEqual(getInt(res3), getInt(res2))
        res4 = self.add_1n.execute([res1])[0]
        self.assertEqual(getInt(res4), getInt(res1) + 1)
        res5 = self.add_nn.execute([res1, Natural([1])])[0]
        self.assertEqual(getInt(res5), getInt(res4))
        res6 = self.com_nn.execute([res4, res5])[0]
        self.assertEqual(getInt(res6), 0)
        res7 = self.com_nn.execute([res1, self.n2])[0]
        self.assertEqual(getInt(res7), 2)
        res8 = self.com_nn.execute([self.n3, res1])[0]
        self.assertEqual(getInt(res8), 1)
        res9 = self.com_nn.execute([res4, res5])[0]
        self.assertEqual(getInt(res9), 0)
        res10 = self.sub_nn.execute([self.n2, self.n1])[0]
        self.assertEqual(getInt(res10), getInt(self.n2) - getInt(self.n1))
        res11 = self.sub_nn.execute([res1, self.n2])[0]
        self.assertEqual(getInt(res11), getInt(self.n3))
        res12 = self.sub_nn.execute([res1, self.n3])[0]
        self.assertEqual(getInt(self.n2), getInt(self.n2_c))
        self.assertEqual(getInt(res1), getInt(self.n2) + getInt(self.n3))
        self.assertEqual(getInt(res1) - getInt(self.n3), getInt(self.n2))
        self.assertEqual(getInt(res12), getInt(res1) - getInt(self.n3))

        #УМНОЖЕНИЯ И ДЕЛЕНИЯ
        res13 = self.div_nn.execute([res1, self.n1])[0]
        res14 = self.mod_nn.execute([res1, self.n1])[0]
        self.assertEqual(getInt(res13), getInt(res1) // getInt(self.n1))

if __name__ == '__main__':
    unittest.main()
