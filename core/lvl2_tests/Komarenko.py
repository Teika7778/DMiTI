import unittest
from core.RED_Q_Q import RED_Q_Q # Сокращение дроби
from core.INT_Q_B import INT_Q_B # Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
from core.TRANS_Q_Z import TRANS_Q_Z # Преобразование сокращенного дробного в целое (если знаменатель равен 1)
from core.ADD_QQ_Q import ADD_QQ_Q # Сложение дробей
from core.SUB_QQ_Q import SUB_QQ_Q # Вычитание дробей

from data_types import *

def getInt(n):
    return int("".join(list(map(str, n.numbers[::-1]))))


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.red_qq = RED_Q_Q()   # +
        self.int_qq = INT_Q_B()   # +
        self.trans_qz = TRANS_Q_Z()   # +
        self.add_qq = ADD_QQ_Q()   # +
        self.sub_qq = SUB_QQ_Q()   # +

        self.r1 = Rational(Integer(Natural([1]*100), is_positive=True),Natural([1] * 100))
        self.r2 = Rational(Integer(Natural([9]*100), is_positive=True),Natural([1] * 100))
        self.r2_red = Rational(Integer(Natural([8] + [9] * 14 +[1]), is_positive=True),Natural([2]))

    def testsRationalBigNumbers(self):
        #СЛОЖЕНИЕ, ВЫЧИТАНИЕ
        resAdd = self.add_qq.execute([self.r1, self.r2])[0]
        expectedAdd = Rational(Integer(Natural([0]+[1]*100), is_positive=True),Natural([1] * 100))

        resSub = self.sub_qq.execute([self.r2, self.r1])[0]
        expectedSub = Rational(Integer(Natural([8]*100), is_positive=True),Natural([1] * 100))

        #СОКРАЩЕНИЕ, СРАВНЕНИЯ
        resRed = self.red_qq.execute([self.r2_red])[0]
        expectedRed = self.r2_red = Rational(Integer(Natural([9]*15), is_positive=True),Natural([1]))
        
        resInt = self.int_qq.execute([resRed])[0]

        resTransQZ = self.trans_qz.execute([resRed])[0]
        expectedResTransQZ = Integer(Natural([9]*15), is_positive=True)
        
        #тесты:
        self.assertEqual(getInt(resRed.numerator.natural), getInt(expectedRed.numerator.natural))
        self.assertEqual(getInt(resRed.denominator), getInt(expectedRed.denominator))

        self.assertEqual(resInt, True)

        self.assertEqual(getInt(resTransQZ.natural),getInt(expectedResTransQZ.natural))

        self.assertEqual(getInt(expectedAdd.numerator.natural), getInt(resAdd.numerator.natural))

        self.assertEqual(getInt(expectedSub.numerator.natural), getInt(resSub.numerator.natural))
if __name__ == '__main__':
    unittest.main()
