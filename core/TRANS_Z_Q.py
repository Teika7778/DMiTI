from core import generic_module as gm
from data_types import *
import copy


class TRANS_Z_Q(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 1: #проверка на получение единственного аргумента
            raise ValueError("Improper arguments: function takes only 1 arg")
        numerator = copy.deepcopy(args[0])
        if not isinstance(numerator, Integer):  # проверка типа
            raise ValueError("Invalid data type: must be integer")
        # Создаём объект класса Natural для знамянателя и обьект класса Rational, представляющий дробь z/1
        denominator = Natural([1])
        rational_number = Rational(numerator, denominator)
        return rational_number
    def reference(self) -> str:
        pass