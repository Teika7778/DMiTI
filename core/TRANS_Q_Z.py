from core import generic_module as gm
from data_types import *
import copy


class TRANS_Q_Z(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 1: #проверка на получение единственного аргумента
            raise ValueError("Improper arguments: function takes only 1 arg")
        rational = copy.deepcopy(args[0])
        if not isinstance(rational, Rational):  # проверка типа
            raise ValueError("Invalid data type: must be rational")
        if not (rational.denominator.numbers == [1]):
            raise ValueError("Invalid data type: must be reduced rational")
        # Создаём объект класса Integer из знамянателя
        result_integer = Integer(Natural(rational.numerator.natural.numbers), rational.numerator.is_positive)
        return result_integer
    
    def reference(self) -> str:
        pass