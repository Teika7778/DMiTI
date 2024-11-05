import unittest
from core.ADD_ZZ_Z import ADD_ZZ_Z
from core.DIV_ZZ_Z import DIV_ZZ_Z
from core.MUL_ZZ_Z import MUL_ZM_Z, MUL_ZZ_Z
from core.SUB_ZZ_Z import SUB_ZZ_Z
from data_types import *

def getInt(n):
    return int("".join(list(map(str, n.natural.numbers[::-1]))))


#(4566789+54734984)*(-3837643736)-32748273453*(-3654264235//5)

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.add_zz = ADD_ZZ_Z()   # +
        self.div_zz = DIV_ZZ_Z()   # +
        self.mul_zz = MUL_ZZ_Z()   # +
        self.sub_zz = SUB_ZZ_Z()   # +

        self.n1 = Integer(Natural([9, 8, 7, 6, 6, 5, 4]), True)
        self.n2 = Integer(Natural([4, 8, 9, 4, 3, 7, 4, 5]), True)
        self.n3 = Integer(Natural([6, 3, 7, 3, 4, 6, 7, 3, 8, 3]), False)
        self.n4 = Integer(Natural([3, 5, 4, 3, 7, 2, 8, 4, 7, 2, 3]), True)
        self.n5 = Integer(Natural([5, 3, 2, 4, 6, 2, 4, 5, 6, 3]), False)
        self.n6 = Integer(Natural([5]), True)
        self.answer = Integer(Natural([3, 6, 7, 6, 2, 4, 2, 7, 7, 9, 0, 8, 9, 8, 5, 6 ,0 ,7 ,3, 2]), True)


    def testlonginteger(self):
        res1 = self.add_zz.execute([self.n1, self.n2])[0]
        self.assertEqual(getInt(res1), getInt(self.n1) + getInt(self.n2))
        res2 = self.mul_zz.execute([res1, self.n3])[0]
        self.assertEqual(getInt(res2), getInt(res1) * getInt(self.n3))
        res3 = self.mul_zz.execute([self.n4, self.n5])[0]
        self.assertEqual(getInt(res3), getInt(self.n4) * getInt(self.n5))
        res4 = self.div_zz.execute([res3, self.n6])[0]
        self.assertEqual(getInt(res4), getInt(res3) // getInt(self.n6))
        res5 = self.sub_zz.execute([res2, res4])[0]
        self.assertEqual(getInt(self.answer), getInt(res5))







if __name__ == '__main__':
    unittest.main()
